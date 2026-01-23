"""TypeScript structure extraction using tree-sitter.

Extracts functional structure from TypeScript code for order-independent comparison.
"""

from pathlib import Path

from tree_sitter import Parser


def extract_interfaces(code: bytes, parser: Parser) -> list[dict]:
    """Extract interface definitions from TypeScript code.

    Returns:
        List of interfaces sorted by name, each containing:
        - name: Interface name
        - properties: List of {name, type, optional} dicts sorted by name
    """
    tree = parser.parse(code)
    interfaces = []

    for node in _find_nodes(tree.root_node, "interface_declaration"):
        name_node = node.child_by_field_name("name")
        if not name_node:
            continue

        body_node = node.child_by_field_name("body")
        if not body_node:
            continue

        properties = []
        for prop_node in _find_nodes(body_node, "property_signature"):
            prop_name = None
            prop_type = None
            optional = False

            for child in prop_node.children:
                if child.type == "property_identifier":
                    prop_name = child.text.decode("utf-8")
                elif child.type == "?":
                    optional = True
                elif child.type == "type_annotation":
                    # Get the type inside the annotation (skip the colon)
                    for type_child in child.children:
                        if type_child.type != ":":
                            prop_type = type_child.text.decode("utf-8")
                            break

            if prop_name and prop_type:
                properties.append(
                    {
                        "name": prop_name,
                        "type": prop_type,
                        "optional": optional,
                    }
                )

        interfaces.append(
            {
                "name": name_node.text.decode("utf-8"),
                "properties": sorted(properties, key=lambda p: p["name"]),
            }
        )

    return sorted(interfaces, key=lambda i: i["name"])


def extract_functions(code: bytes, parser: Parser) -> list[dict]:
    """Extract function definitions from TypeScript code.

    Returns:
        List of functions sorted by name, each containing:
        - name: Function name
        - params: List of {name, type} dicts in declaration order
        - return_type: Return type string or None
    """
    tree = parser.parse(code)
    functions = []

    for node in _find_nodes(tree.root_node, "function_declaration"):
        name_node = node.child_by_field_name("name")
        if not name_node:
            continue

        params = []
        params_node = node.child_by_field_name("parameters")
        if params_node:
            for param_node in _find_nodes(params_node, "required_parameter"):
                param_name = None
                param_type = None
                for child in param_node.children:
                    if child.type == "identifier":
                        param_name = child.text.decode("utf-8")
                    elif child.type == "type_annotation":
                        for type_child in child.children:
                            if type_child.type != ":":
                                param_type = type_child.text.decode("utf-8")
                                break
                if param_name:
                    params.append({"name": param_name, "type": param_type})

        return_type = None
        return_type_node = node.child_by_field_name("return_type")
        if return_type_node:
            for child in return_type_node.children:
                if child.type != ":":
                    return_type = child.text.decode("utf-8")
                    break

        functions.append(
            {
                "name": name_node.text.decode("utf-8"),
                "params": params,
                "return_type": return_type,
            }
        )

    return sorted(functions, key=lambda f: f["name"])


def extract_type_aliases(code: bytes, parser: Parser) -> list[dict]:
    """Extract type alias definitions from TypeScript code.

    Returns:
        List of type aliases sorted by name, each containing:
        - name: Type alias name
        - definition: The type definition string
    """
    tree = parser.parse(code)
    aliases = []

    for node in _find_nodes(tree.root_node, "type_alias_declaration"):
        name_node = node.child_by_field_name("name")
        value_node = node.child_by_field_name("value")

        if name_node and value_node:
            aliases.append(
                {
                    "name": name_node.text.decode("utf-8"),
                    "definition": value_node.text.decode("utf-8"),
                }
            )

    return sorted(aliases, key=lambda a: a["name"])


def extract_enums(code: bytes, parser: Parser) -> list[dict]:
    """Extract enum and const-object-as-enum definitions from TypeScript code.

    Returns:
        List of enums sorted by name, each containing:
        - name: Enum name
        - members: List of {name, value} dicts sorted by name
    """
    tree = parser.parse(code)
    enums = []

    # Handle TypeScript enums
    for node in _find_nodes(tree.root_node, "enum_declaration"):
        name_node = node.child_by_field_name("name")
        body_node = node.child_by_field_name("body")

        if not name_node or not body_node:
            continue

        members = []
        for member_node in _find_nodes(body_node, "enum_assignment"):
            member_name = None
            member_value = None
            for child in member_node.children:
                if child.type == "property_identifier":
                    member_name = child.text.decode("utf-8")
                elif child.type == "string":
                    member_value = child.text.decode("utf-8")
            if member_name and member_value:
                members.append({"name": member_name, "value": member_value})

        enums.append(
            {
                "name": name_node.text.decode("utf-8"),
                "members": sorted(members, key=lambda m: m["name"]),
            }
        )

    # Handle const objects used as enums (export const X = {...} as const)
    for node in _find_nodes(tree.root_node, "lexical_declaration"):
        # Check if this is a const
        is_const = any(child.type == "const" for child in node.children)
        if not is_const:
            continue

        for var_decl in _find_nodes(node, "variable_declarator"):
            name_node = var_decl.child_by_field_name("name")
            value_node = var_decl.child_by_field_name("value")

            if not name_node or not value_node:
                continue

            # Check for "as const" assertion with object literal
            if value_node.type == "as_expression":
                obj_node = None
                for child in value_node.children:
                    if child.type == "object":
                        obj_node = child
                        break

                if obj_node:
                    members = []
                    for pair_node in _find_nodes(obj_node, "pair"):
                        key_node = pair_node.child_by_field_name("key")
                        val_node = pair_node.child_by_field_name("value")
                        if key_node and val_node:
                            members.append(
                                {
                                    "name": key_node.text.decode("utf-8"),
                                    "value": val_node.text.decode("utf-8"),
                                }
                            )

                    if members:
                        enums.append(
                            {
                                "name": name_node.text.decode("utf-8"),
                                "members": sorted(members, key=lambda m: m["name"]),
                            }
                        )

    return sorted(enums, key=lambda e: e["name"])


def extract_exports(code: bytes, parser: Parser) -> list[str]:
    """Extract exported names from TypeScript code.

    Returns:
        List of exported names (sorted, unique).
    """
    tree = parser.parse(code)
    exports = set()

    # Handle export statements (export { X, Y })
    for node in _find_nodes(tree.root_node, "export_statement"):
        # Check for named exports: export { X, Y } or export { X } from './module'
        for clause in _find_nodes(node, "export_clause"):
            for spec in _find_nodes(clause, "export_specifier"):
                name_node = spec.child_by_field_name("name")
                if name_node:
                    exports.add(name_node.text.decode("utf-8"))

        # Check for declaration exports (export interface X, export function Y, etc.)
        for child in node.children:
            if child.type == "interface_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "function_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "lexical_declaration":
                for var_decl in _find_nodes(child, "variable_declarator"):
                    name = var_decl.child_by_field_name("name")
                    if name:
                        exports.add(name.text.decode("utf-8"))
            elif child.type == "type_alias_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "enum_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "class_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))

    return sorted(exports)


def extract_classes(code: bytes, parser: Parser) -> list[dict]:
    """Extract class definitions from TypeScript code.

    Returns:
        List of classes sorted by name, each containing:
        - name: Class name
        - properties: List of {name, type, optional} dicts sorted by name
        - methods: List of {name, params, return_type} dicts sorted by name
    """
    tree = parser.parse(code)
    classes = []

    for node in _find_nodes(tree.root_node, "class_declaration"):
        name_node = node.child_by_field_name("name")
        body_node = node.child_by_field_name("body")

        if not name_node or not body_node:
            continue

        properties = []
        methods = []

        for child in body_node.children:
            # Public field definition (property)
            if child.type == "public_field_definition":
                prop_name = None
                prop_type = None
                optional = False

                for field_child in child.children:
                    if field_child.type == "property_identifier":
                        prop_name = field_child.text.decode("utf-8")
                    elif field_child.type == "?":
                        optional = True
                    elif field_child.type == "type_annotation":
                        for type_child in field_child.children:
                            if type_child.type != ":":
                                prop_type = type_child.text.decode("utf-8")
                                break

                if prop_name and prop_type:
                    properties.append(
                        {
                            "name": prop_name,
                            "type": prop_type,
                            "optional": optional,
                        }
                    )

            # Method definition
            elif child.type == "method_definition":
                method_name_node = child.child_by_field_name("name")
                if not method_name_node:
                    continue

                method_name = method_name_node.text.decode("utf-8")
                if method_name == "constructor":
                    continue  # Skip constructor

                params = []
                params_node = child.child_by_field_name("parameters")
                if params_node:
                    for param_node in _find_nodes(params_node, "required_parameter"):
                        param_name = None
                        param_type = None
                        for p_child in param_node.children:
                            if p_child.type == "identifier":
                                param_name = p_child.text.decode("utf-8")
                            elif p_child.type == "type_annotation":
                                for type_child in p_child.children:
                                    if type_child.type != ":":
                                        param_type = type_child.text.decode("utf-8")
                                        break
                        if param_name:
                            params.append({"name": param_name, "type": param_type})

                return_type = None
                return_type_node = child.child_by_field_name("return_type")
                if return_type_node:
                    for rt_child in return_type_node.children:
                        if rt_child.type != ":":
                            return_type = rt_child.text.decode("utf-8")
                            break

                methods.append(
                    {
                        "name": method_name,
                        "params": params,
                        "return_type": return_type,
                    }
                )

        classes.append(
            {
                "name": name_node.text.decode("utf-8"),
                "properties": sorted(properties, key=lambda p: p["name"]),
                "methods": sorted(methods, key=lambda m: m["name"]),
            }
        )

    return sorted(classes, key=lambda c: c["name"])


def extract_ts_structure(directory: Path, parser: Parser) -> dict:
    """Extract functional structure from all .ts files in directory.

    Returns:
        {
            "relative/path/to/file.ts": {
                "interfaces": [...],
                "functions": [...],
                "type_aliases": [...],
                "enums": [...],
                "classes": [...],
                "exports": [...]
            }
        }
    """
    result = {}

    for ts_file in sorted(directory.rglob("*.ts")):
        rel_path = str(ts_file.relative_to(directory))
        code = ts_file.read_bytes()

        result[rel_path] = {
            "interfaces": extract_interfaces(code, parser),
            "functions": extract_functions(code, parser),
            "type_aliases": extract_type_aliases(code, parser),
            "enums": extract_enums(code, parser),
            "classes": extract_classes(code, parser),
            "exports": extract_exports(code, parser),
        }

    return result


def _find_nodes(node, node_type: str) -> list:
    """Recursively find all nodes of a given type."""
    results = []
    if node.type == node_type:
        results.append(node)
    for child in node.children:
        results.extend(_find_nodes(child, node_type))
    return results

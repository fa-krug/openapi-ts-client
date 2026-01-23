"""TypeScript structure extraction using tree-sitter.

Extracts functional structure from TypeScript code for order-independent comparison.
"""

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


def _find_nodes(node, node_type: str) -> list:
    """Recursively find all nodes of a given type."""
    results = []
    if node.type == node_type:
        results.append(node)
    for child in node.children:
        results.extend(_find_nodes(child, node_type))
    return results

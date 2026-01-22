"""Tests for extracted type file generation."""

from pathlib import Path

from openapi_ts_client.generators.angular.models import generate_extracted_type_file


class TestGenerateExtractedTypeFile:
    """Tests for generating extracted type files."""

    def test_generates_empty_interface(self, tmp_path: Path):
        """Generates empty interface file for extracted type."""
        output_dir = tmp_path / "model"
        output_dir.mkdir()

        generate_extracted_type_file(
            type_name="Score",
            description="",
            output_dir=output_dir,
            api_title="Test API",
            contact_email="",
        )

        output_file = output_dir / "score.ts"
        assert output_file.exists()
        content = output_file.read_text()
        assert "export interface Score {" in content

    def test_includes_description_as_jsdoc(self, tmp_path: Path):
        """Includes description as JSDoc comment when provided."""
        output_dir = tmp_path / "model"
        output_dir.mkdir()

        generate_extracted_type_file(
            type_name="CodeDuplication",
            description="Percentage of code duplications in main branch",
            output_dir=output_dir,
            api_title="Test API",
            contact_email="",
        )

        output_file = output_dir / "codeDuplication.ts"
        content = output_file.read_text()
        assert "Percentage of code duplications in main branch" in content
        assert "export interface CodeDuplication {" in content

    def test_returns_filename_without_extension(self, tmp_path: Path):
        """Returns filename without .ts extension for barrel export."""
        output_dir = tmp_path / "model"
        output_dir.mkdir()

        result = generate_extracted_type_file(
            type_name="TestCoverage",
            description="",
            output_dir=output_dir,
            api_title="Test API",
            contact_email="",
        )

        assert result == "testCoverage"

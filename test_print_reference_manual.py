"""Test print_reference_manual generation functions"""
from print_reference_manual import (
    generate_text_reference,
    generate_markdown_reference,
    generate_csv_reference
)


def test_generate_text_reference():
    """Test plain text reference manual generation."""
    reference = generate_text_reference()
    lines = reference.split('\n')
    assert len(lines) >= 29
    assert "1" in reference and "White" in reference and "Blue" in reference
    assert "25" in reference and "Violet" in reference and "Slate" in reference


def test_generate_markdown_reference():
    """Test Markdown format reference manual generation."""
    reference = generate_markdown_reference()
    lines = reference.split('\n')
    assert len(lines) >= 27
    assert "| Pair Number | Major Color | Minor Color |" in reference
    assert "| --- | --- | --- |" in reference


def test_generate_csv_reference():
    """Test CSV format reference manual generation."""
    reference = generate_csv_reference()
    lines = reference.split('\n')
    assert len(lines) >= 26
    assert reference.startswith("Pair Number,Major Color,Minor Color")
    assert "1,White,Blue" in reference
    assert "25,Violet,Slate" in reference

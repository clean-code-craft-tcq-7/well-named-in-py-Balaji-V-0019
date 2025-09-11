"""Test reference manual generation functions"""
import pytest
from colors import MAJOR_COLORS, MINOR_COLORS
from print_reference_manual import (
    color_index_pair_number,
    get_csv_header,
    get_csv_row,
    get_md_header,
    get_md_row,
    get_text_header,
    get_text_row,
    generate_text_reference,
    generate_markdown_reference,
    generate_csv_reference
)


def test_color_index_pair_number():
    """Test color index to pair number calculation."""
    assert color_index_pair_number(0, 0) == 1
    assert color_index_pair_number(4, 4) == 25


def test_get_text_header():
    """Test plain text header format."""
    header = get_text_header()
    assert "25-Pair Color Code Reference Manual" in header
    assert "=" in header
    assert "Pair Number | Major Color | Minor Color" in header


def test_get_text_row():
    """Test plain text row format."""
    row = get_text_row(1, MAJOR_COLORS[0], MINOR_COLORS[0])
    assert "1" in row
    assert MAJOR_COLORS[0] in row
    assert MINOR_COLORS[0] in row


def test_get_md_header():
    """Test Markdown header format."""
    md_header = get_md_header()
    expected = "| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n"
    assert expected in md_header


def test_get_md_row():
    """Test Markdown row format."""
    md_row = get_md_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"| 1 | {MAJOR_COLORS[1]} | {MINOR_COLORS[1]} |\n"
    assert expected in md_row


def test_get_csv_header():
    """Test CSV header format."""
    csv_header = get_csv_header()
    assert "Pair Number,Major Color,Minor Color\n" in csv_header


def test_get_csv_row():
    """Test CSV row format."""
    csv_row = get_csv_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"1,{MAJOR_COLORS[1]},{MINOR_COLORS[1]}\n"
    assert expected in csv_row


def test_generate_text_reference():
    """Test complete text reference generation."""
    reference = generate_text_reference()
    lines = reference.split('\n')
    
    # Should have header + 25 data lines + empty line at end
    assert len(lines) >= 29
    
    # Check for first and last entries
    assert "1" in reference and "White" in reference and "Blue" in reference
    assert "25" in reference and "Violet" in reference and "Slate" in reference


def test_generate_markdown_reference():
    """Test complete Markdown reference generation."""
    reference = generate_markdown_reference()
    lines = reference.split('\n')
    
    # Should have header (2 lines) + 25 data lines + empty line at end
    assert len(lines) >= 27
    
    # Check Markdown format
    assert "| Pair Number | Major Color | Minor Color |" in reference
    assert "| --- | --- | --- |" in reference


def test_generate_csv_reference():
    """Test complete CSV reference generation."""
    reference = generate_csv_reference()
    lines = reference.split('\n')
    
    # Should have header + 25 data lines + empty line at end
    assert len(lines) >= 26
    
    # Check CSV format
    assert reference.startswith("Pair Number,Major Color,Minor Color")
    assert "1,White,Blue" in reference
    assert "25,Violet,Slate" in reference


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

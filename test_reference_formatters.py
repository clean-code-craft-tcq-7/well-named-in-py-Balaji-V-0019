"""Test reference manual formatters"""
from colors import MAJOR_COLORS, MINOR_COLORS
from reference_formatters import (
    get_csv_header,
    get_csv_row,
    get_md_header,
    get_md_row,
    get_text_header,
    get_text_row
)


def test_get_text_header():
    """Test plain text header."""
    header = get_text_header()
    assert "25-Pair Color Code Reference Manual" in header
    assert "=" in header
    assert "Pair Number | Major Color | Minor Color" in header


def test_get_text_row():
    """Test plain text row."""
    row = get_text_row(1, MAJOR_COLORS[0], MINOR_COLORS[0])
    assert "1" in row
    assert MAJOR_COLORS[0] in row
    assert MINOR_COLORS[0] in row


def test_get_md_header():
    """Test Markdown header."""
    md_header = get_md_header()
    expected = "| Pair Number | Major Color |"
    expected += " Minor Color |\n| --- | --- | --- |\n"
    assert expected in md_header


def test_get_md_row():
    """Test Markdown row."""
    md_row = get_md_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"| 1 | {MAJOR_COLORS[1]} | {MINOR_COLORS[1]} |\n"
    assert expected in md_row


def test_get_csv_header():
    """Test CSV header."""
    csv_header = get_csv_header()
    assert "Pair Number,Major Color,Minor Color\n" in csv_header


def test_get_csv_row():
    """Test CSV row."""
    csv_row = get_csv_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"1,{MAJOR_COLORS[1]},{MINOR_COLORS[1]}\n"
    assert expected in csv_row

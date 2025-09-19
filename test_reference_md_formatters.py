"""Test markdown formatters"""
from colors import MAJOR_COLORS, MINOR_COLORS
from reference_formatters import get_md_header, get_md_row


def test_get_md_header():
    """Test Markdown header formatting."""
    md_header = get_md_header()
    expected = "| Pair Number | Major Color |"
    expected += " Minor Color |\n| --- | --- | --- |\n"
    assert expected in md_header


def test_get_md_row():
    """Test Markdown row formatting."""
    md_row = get_md_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"| 1 | {MAJOR_COLORS[1]} | {MINOR_COLORS[1]} |\n"
    assert expected in md_row

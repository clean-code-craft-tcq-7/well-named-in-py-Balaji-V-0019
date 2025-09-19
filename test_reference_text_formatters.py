"""Test text and markdown formatters"""
from colors import MAJOR_COLORS, MINOR_COLORS
from reference_formatters import get_text_header, get_text_row


def test_get_text_header():
    """Test text header formatting."""
    header = get_text_header()
    assert "25-Pair Color Code Reference Manual" in header
    assert "=" in header
    assert "Pair Number | Major Color | Minor Color" in header


def test_get_text_row():
    """Test text row formatting."""
    row = get_text_row(1, MAJOR_COLORS[0], MINOR_COLORS[0])
    assert "1" in row
    assert MAJOR_COLORS[0] in row
    assert MINOR_COLORS[0] in row

"""Test CSV formatters"""
from colors import MAJOR_COLORS, MINOR_COLORS
from reference_formatters import get_csv_header, get_csv_row


def test_get_csv_header():
    """Test CSV header formatting."""
    csv_header = get_csv_header()
    assert "Pair Number,Major Color,Minor Color\n" in csv_header


def test_get_csv_row():
    """Test CSV row formatting."""
    csv_row = get_csv_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    expected = f"1,{MAJOR_COLORS[1]},{MINOR_COLORS[1]}\n"
    assert expected in csv_row

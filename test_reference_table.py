"""Test reference table logic"""
from reference_table import color_index_pair_number


def test_color_index_pair_number():
    """Test color index to pair number calculation."""
    assert color_index_pair_number(0, 0) == 1
    assert color_index_pair_number(4, 4) == 25

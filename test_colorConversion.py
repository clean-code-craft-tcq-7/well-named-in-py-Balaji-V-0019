"""Test color conversion functions"""
import pytest
from convert_color import (get_color_from_pair_number,
                           get_pair_number_from_color)


@pytest.mark.parametrize(
    "pair_number,expected_major_color,expected_minor_color",
    [(4, 'White', 'Brown'), (5, 'White', 'Slate')],
)
def test_number_to_pair(pair_number, expected_major_color,
                        expected_minor_color):
    """Test conversion from pair number to color pair."""
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color


@pytest.mark.parametrize(
    "major_color,minor_color,expected_pair_number",
    [('Black', 'Orange', 12), ('Violet', 'Slate', 25), ('Red', 'Orange', 7)],
)
def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """Test conversion from color pair to pair number."""
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

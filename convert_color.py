"""Conversion functions for color pairs"""
from colors import MAJOR_COLORS, MINOR_COLORS


def color_pair_to_string(major_color, minor_color):
    """Convert a color pair to a string."""
    return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
    """Get color from pair number."""
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise ValueError('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise ValueError('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    """Get pair number from color."""
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError as e:
        raise ValueError('Major index out of range') from e
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError as e:
        raise ValueError('Minor index out of range') from e
    return major_index * len(MINOR_COLORS) + minor_index + 1

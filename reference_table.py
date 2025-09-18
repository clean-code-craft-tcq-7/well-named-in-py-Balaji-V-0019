"""Reference table generation using strategy pattern"""
from colors import MAJOR_COLORS, MINOR_COLORS


def color_index_pair_number(major_color_index, minor_color_index):
    """Calculate pair number from color indices."""
    return major_color_index * len(MINOR_COLORS) + minor_color_index + 1


def form_reference_table(header_formatter, row_formatter):
    """Form reference table using provided header and row formatters."""
    table_string = header_formatter()
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            pair_num = color_index_pair_number(i, j)
            table_string += row_formatter(pair_num, major, minor)
    return table_string

"""Reference manual generation with multiple format support"""
from colors import MAJOR_COLORS, MINOR_COLORS


def color_index_pair_number(major_color_index, minor_color_index):
    """Calculate pair number from color indices."""
    return major_color_index * len(MINOR_COLORS) + minor_color_index + 1


def get_text_header():
    """Get header for plain text format."""
    header = "25-Pair Color Code Reference Manual\n"
    header += "=" * 40 + "\n"
    header += "Pair Number | Major Color | Minor Color\n"
    header += "-" * 40 + "\n"
    return header


def get_text_row(pair_num, major_color, minor_color):
    """Get row for plain text format."""
    return f"{pair_num:11} | {major_color:11} | {minor_color}\n"


def get_md_header():
    """Get header for Markdown table format."""
    return "| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n"


def get_md_row(pair_num, major_color, minor_color):
    """Get row for Markdown table format."""
    return f"| {pair_num} | {major_color} | {minor_color} |\n"


def get_csv_header():
    """Get header for CSV format."""
    return "Pair Number,Major Color,Minor Color\n"


def get_csv_row(pair_num, major_color, minor_color):
    """Get row for CSV format."""
    return f"{pair_num},{major_color},{minor_color}\n"


def form_reference_table(header_formatter, row_formatter):
    """Generate reference table using strategy pattern."""
    table_string = header_formatter()
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            pair_num = color_index_pair_number(i, j)
            table_string += row_formatter(pair_num, major, minor)
    return table_string


def generate_text_reference():
    """Generate plain text reference manual."""
    return form_reference_table(get_text_header, get_text_row)


def generate_markdown_reference():
    """Generate Markdown table reference manual."""
    return form_reference_table(get_md_header, get_md_row)


def generate_csv_reference():
    """Generate CSV reference manual."""
    return form_reference_table(get_csv_header, get_csv_row)


def print_text_reference():
    """Print plain text reference manual."""
    print(generate_text_reference())


def print_markdown_reference():
    """Print Markdown table reference manual."""
    print(generate_markdown_reference())


def print_csv_reference():
    """Print CSV reference manual."""
    print(generate_csv_reference())

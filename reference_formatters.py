"""Header and row formatter functions for reference manual"""


def get_text_header():
    """Get plain text header."""
    text_header = "25-Pair Color Code Reference Manual\n"
    text_header = text_header + "=" * 40 + "\n"
    text_header = text_header + "Pair Number | Major Color | Minor Color\n"
    text_header = text_header + "-" * 40 + "\n"
    return text_header


def get_text_row(pair_num, major_color, minor_color):
    """Get plain text row."""
    return f"{pair_num:11} | {major_color:11} | {minor_color}\n"


def get_md_header():
    """Get Markdown header."""
    return "| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n"


def get_md_row(pair_num, major_color, minor_color):
    """Get Markdown row."""
    return f"| {pair_num} | {major_color} | {minor_color} |\n"


def get_csv_header():
    """Get CSV header."""
    return "Pair Number,Major Color,Minor Color\n"


def get_csv_row(pair_num, major_color, minor_color):
    """Get CSV row."""
    return f"{pair_num},{major_color},{minor_color}\n"

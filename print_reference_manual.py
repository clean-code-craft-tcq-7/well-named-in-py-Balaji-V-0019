
"""Print functions for reference manual formats"""
from reference_formatters import (
    get_text_header, get_text_row,
    get_md_header, get_md_row,
    get_csv_header, get_csv_row
)
from reference_table import form_reference_table


def generate_text_reference():
    """Generate plain text reference manual."""
    return form_reference_table(get_text_header, get_text_row)


def generate_markdown_reference():
    """Generate Markdown format reference manual."""
    return form_reference_table(get_md_header, get_md_row)


def generate_csv_reference():
    """Generate CSV format reference manual."""
    return form_reference_table(get_csv_header, get_csv_row)


def print_text_reference():
    """Print plain text reference manual."""
    print(generate_text_reference())


def print_markdown_reference():
    """Print Markdown format reference manual."""
    print(generate_markdown_reference())


def print_csv_reference():
    """Print CSV format reference manual."""
    print(generate_csv_reference())

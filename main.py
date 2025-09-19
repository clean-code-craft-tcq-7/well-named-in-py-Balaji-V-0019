"""Main script"""
from convert_color import get_color_from_pair_number
from convert_color import get_pair_number_from_color
from print_reference_manual import print_text_reference
from print_reference_manual import generate_markdown_reference
from print_reference_manual import generate_csv_reference


def main():
    """Demonstrates color code conversions and print reference manuals."""
    print("25-Pair Color Code Conversion System\n" + "=" * 40)
    print("\n1. Basic Color Conversion Examples:\n" + "-" * 35)
    major, minor = get_color_from_pair_number(12)
    print(f"Pair 12 -> {major} {minor}")
    pair_number = get_pair_number_from_color('Violet', 'Slate')
    print(f"Violet Slate -> Pair {pair_number}")
    print("\n2. Plain Text Reference Manual:\n" + "-" * 35)
    print_text_reference()
    print("\n3. Markdown Table Format:\n" + "-" * 28)
    print(generate_markdown_reference())
    print("\n4. CSV Format Reference:\n" + "-" * 25)
    print(generate_csv_reference())
    print("\n" + "=" * 40 + "\nSystem ready for use!")


if __name__ == "__main__":
    main()

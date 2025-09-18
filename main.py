"""Main script"""
from convert_color import get_color_from_pair_number
from convert_color import get_pair_number_from_color
from print_reference_manual import (
    print_text_reference,
    generate_markdown_reference,
    generate_csv_reference
)


def main():
    """ Main function """
    print("25-Pair Color Code Conversion System")
    print("=" * 40)

    # Demonstrate basic conversion functions
    print("\n1. Basic Color Conversion Examples:")
    print("-" * 35)

    # Example: pair number to colors
    major, minor = get_color_from_pair_number(12)
    print(f"Pair 12 -> {major} {minor}")

    # Example: colors to pair number
    pair_num = get_pair_number_from_color('Violet', 'Slate')
    print(f"Violet Slate -> Pair {pair_num}")

    # Display reference manual in text format
    print("\n2. Plain Text Reference Manual:")
    print("-" * 35)
    print_text_reference()

    # Display Markdown format
    print("\n3. Markdown Table Format:")
    print("-" * 28)
    markdown_content = generate_markdown_reference()
    print(markdown_content)

    # Generate CSV format
    print("\n4. CSV Format Reference:")
    print("-" * 25)
    csv_content = generate_csv_reference()
    print(csv_content)

    print("\n" + "=" * 40)
    print("System ready for use!")


if __name__ == "__main__":
    main()

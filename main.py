import sys
from stats import get_num_words, get_num_characters, sort_characters

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath) as file:
        return file.read()

def main():
    # Check if the user provided a book file path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with a status code of 1

    # Relative path to the frankenstein.txt file
    filepath = sys.argv[1]
    
    # Get the text of the book
    book_text = get_book_text(filepath)

    # Get the number of words in the string
    num_words = get_num_words(book_text)

    # Count the frequency of each character in the book
    char_count = get_num_characters(book_text)
    
    # Sort the characters by frequency
    sorted_chars = sort_characters(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
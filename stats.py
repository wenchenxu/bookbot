def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1  # Increment count if character exists
        else:
            char_count[char] = 1   # Initialize count if character is new
    return char_count

def sort_characters(char_count):
    """Converts the character count dictionary into a sorted list of dictionaries."""
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list

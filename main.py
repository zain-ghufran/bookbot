import sys
# --------------------------
import sys
print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# ----------------------------------
from stats import count_words, character_counter, dic_sort

# Opens txt 
def get_book_text(filepath):
    # with grabs the file and stores it as book
    with open(filepath) as book:
        # converts txt to a string
        contents = book.read()
    return contents


def main():
    # this is the path to our file
    path = sys.argv[1]
    # this variable uses the previous function to convert the txt into a string
    text = get_book_text(path)
    # this variable utilizes the count_words function from stats.py to count words
    word_count = count_words(text)
    # same thing but for characters
    c_count = character_counter(text)
    print( f"{word_count} words found in the document")
    print(c_count)
    return path, text, word_count, c_count
    

def generate_report(path, word_count):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
          """)
    for item in dic_sort(c_count):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    



path, text, word_count, c_count = main()
generate_report(path, word_count)

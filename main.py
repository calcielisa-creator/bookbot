import sys
from stats import count_words, count_chars, sorted_list
def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def main ():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    f = get_book_text(book_path)
    num_words = count_words(f)
    counter = count_chars(f)
    print("============ BOOKBOT ============\nAnalyzing book found at", book_path, "...\n----------- Word Count ----------\nFound", num_words, "total words\n--------- Character Count -------")
    list = sorted_list(counter) 
    for d in list:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")
main ()
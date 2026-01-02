from stats import count_words
def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def main ():
    f = get_book_text("books/frankenstein.txt")
    num_words = count_words(f)
    print("Found", num_words, "total words")
main ()
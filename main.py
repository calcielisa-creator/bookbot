from stats import count_words, count_chars
def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def main ():
    f = get_book_text("books/frankenstein.txt")
    num_words = count_words(f)
    counter = count_chars(f)
    print("Found", num_words, "total words")
    print(counter)
main ()
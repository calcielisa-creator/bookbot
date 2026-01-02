def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def count_words (text):
    num= len(text.split())
    return num
def main ():
    f = get_book_text("books/frankenstein.txt")
    num_words = count_words(f)
    print("Found", num_words, "total words")
main ()
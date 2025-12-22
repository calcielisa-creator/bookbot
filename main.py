def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def main ():
    f = get_book_text("books/frankenstein.txt")
    print(f)
main ()
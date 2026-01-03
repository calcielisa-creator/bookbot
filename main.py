from stats import count_words, count_chars, sorted_list
def get_book_text (path):
    with open(path) as f:
        content = f.read()
    return content
def main ():
    f = get_book_text("books/frankenstein.txt")
    num_words = count_words(f)
    counter = count_chars(f)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound", num_words, "total words\n--------- Character Count -------")
    list = sorted_list(counter) 
    for d in list:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")
main ()
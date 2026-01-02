def count_words (text):
    num= len(text.split())
    return num
def count_chars (text):
    text = text.lower()
    counter = {}
    for i in range(0, len(text)):
        if text[i] in counter:
            counter[text[i]] += 1
        else:
            counter[text[i]] = 1  
    return counter
def sorted_list(counter):
    list = []
    for i in counter:
        if i.isalpha():
            list.append({"char" : i, "num" : counter[i]})
        else:
            continue
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(items):
    return items["num"]   

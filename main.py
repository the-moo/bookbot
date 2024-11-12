#!/usr/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower = text.lower()
    char_count=letters(lower)
    final_report=report(char_count)
    print(final_report)

def sort_on(dict):
    return dict["num"]

def report(char_count):
    output = ""
    checked = [{"char": char, "num": count} for char, count in char_count.items()]
    checked.sort(reverse=True, key=sort_on)
    for char in checked:
        output += f"The '{char['char']}' character was found {char['num']} times\n"
    return output





def letters(lower):
    letter_count = {}
    for let in lower:
        if let.isalpha():
            if let in letter_count:
                letter_count[let] += 1
            else:
                letter_count[let] = 1
   
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


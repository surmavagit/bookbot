def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    lower_case = text.lower()
    for letter in lower_case:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def make_report(path):
    print(f"--- Begin report of {path} ---")
    with open(path) as f:
        file_contents = f.read()

    words = count_words(file_contents)
    print(f"{words} words found in the document\n")

    letter_dict = count_letters(file_contents)
    letter_list = []
    for letter in letter_dict:
        if letter.isalpha():
            letter_list.append({"letter": letter, "number": letter_dict[letter]})

    letter_list.sort(key=lambda x: x["number"], reverse=True)

    for letter in letter_list:
        char = letter["letter"]
        num = letter["number"]
        print(f"The '{char}' character was found {num} times")

    print("--- End report ---")

make_report("books/frankenstein.txt")



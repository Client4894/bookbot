
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    num_letters = count_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

main()

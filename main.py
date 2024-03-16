
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text) # string 
    num_letters = count_letters(text) # dictionary
    sorted_letters = transform_list(num_letters) #dictionary
    
    get_report(book_path, num_words, sorted_letters)


def get_report(book_path, num_words, sorted_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for letter in sorted_letters:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End Report ---")

def transform_list(let_list):
    letters_list = []
    for letter in let_list:
        if letter.isalpha() == True:
            dict_pair = {}
            dict_pair["letter"] = letter
            dict_pair["num"] = let_list[letter]
            letters_list.append(dict_pair)        
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

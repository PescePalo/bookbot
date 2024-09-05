def main():
    book = "books/frankenstein.txt"
    text = book_to_text(book)
    words = n_of_words(text)
    letters = letter_occurance(n_character_appearance(text))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for letter in letters:
        print(f"The {letter['a']} character appears {letter['b']} times")

def book_to_text(book):
    with open(book) as f:
        return f.read()
    
def n_of_words(book_text):
    words = book_text.split()
    return len(words)

def n_character_appearance(text):
    characters = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def letter_occurance(dict):
    letters = []
    characters = []
    
    for i in dict:
        characters.append(i)

    for letter in characters:
        if letter.isalpha() == True:
            letters.append({"a":letter, "b":dict[letter]})
    letters.sort(reverse=True, key=sort_by)  

    return letters
    
        
def sort_by(dict):
    return dict['b']


main()
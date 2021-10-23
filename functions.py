import random
from english_words import words



def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    #picks up a random word from the list of words
    word_letters = set(word)
    user_letters = ""

    print(f"I have thought of a word.\nIt is {len(word)} letters long.\n Can you guess it?")

    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"The letters you have used so far: {user_letters}.")



        letter = input("Input a letter: ").upper()
        if letter in user_letters:
                  print("You have already used this letter. Please input another letter.")
                  continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} is correct.")
        else:
            print("This letter is not in the word")
        user_letters += letter
    print(f"Congratulations! You have guessed the word {word} in {len(user_letters)} tries!")


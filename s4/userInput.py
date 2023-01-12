def belongs_to_dictionary(word):
    with open("tp22/s4/words.txt") as words:
        for i in words:
            if word == i.strip():
                return True
    return False


def ask_word_in_dictionary():
    entered = input("Player 1, please enter a word: ")
    while not belongs_to_dictionary(entered):
        entered = input("Player 1, please enter an other word: ")
    return entered


def is_one_letter(s):
    return len(s) == 1 and s.isalpha()


def ask_letter(tried_letters: list):
    letter = input("Player 2, give *one* *letter*: ").lower()

    while letter in tried_letters:
        print("Already used")
        letter = input("Player 2, enter a *new* letter: ").lower()
    else:
        return letter

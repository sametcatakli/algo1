from userInput import *
from hangmanui import *


def main_function():
    word = ask_word_in_dictionary()

    tried_letters = []
    hidden_word = []
    cut_word = []
    max_chances = 10

    for i in range(len(word)):
        hidden_word.append("_")
        cut_word.append(word[i])

    print("Word ok")

    chances = max_chances

    while hidden_word != cut_word:
        if chances == 0:
            print("You lost")
            break

        print("Number of chance(s) remaining:", chances)
        print("Already used letters :", str(tried_letters).replace("[", "").replace("]", "").replace("'", ""))
        print(str(hidden_word).replace(", ", "").replace("[", "").replace("]", "").replace("'", ""))

        letter = ask_letter(tried_letters)

        if (not isinstance(letter, str)) or (len(letter) != 1) or letter == " ":
            print("'" + str(letter) + "'", "is not a letter")
            continue

        tried_letters.append(letter)

        if letter in cut_word:
            for i in range(len(cut_word)):
                if letter == cut_word[i]:
                    hidden_word[i] = letter
            print("'" + str(letter) + "'", "is a right letter")
        else:
            print("'" + str(letter) + "'", "is not a right letter")
            draw_hangman(max_chances - chances)
            chances = chances - 1

    else:
        letters_without_duplicates = []
        for i in range(len(hidden_word)):
            if hidden_word[i] not in letters_without_duplicates:
                letters_without_duplicates.append(hidden_word[i])

        tried_letters_without_right_letters = []
        for i in range(len(tried_letters)):
            if tried_letters[i] not in hidden_word:
                tried_letters_without_right_letters.append(tried_letters[i])

        score = len(letters_without_duplicates) + chances - len(tried_letters_without_right_letters)
        max_score = len(letters_without_duplicates) + max_chances

        print("You won")
        print("Your score is", str(score) + "/" + str(max_score))
        return


main_function()

import random

words = ["python", "apple", "mango", "tiger", "house"]

word = random.choice(words)

guessed = []
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You Won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
        print("Correct Guess!")
    else:
        chances -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)
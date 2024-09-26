import random

def play_hangman():
    animals = ['elephant', 'lion', 'tiger', 'horse']
    word = random.choice(animals)
    hiddenWord = ['_'] * len(word)
    attempts = 6
    triedLetters = []

    print("Welcome to Hangman!")

    while attempts > 0 and '_' in hiddenWord:
        print(f"Word: {' '.join(hiddenWord)}")
        print(f"Remaining attempts: {attempts}")
        print(f"Tried letters: {', '.join(triedLetters)}")

        guess = input("Enter a letter: ").lower()

        if guess in triedLetters:
            print("You've already tried this letter.")
            continue

        triedLetters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hiddenWord[i] = guess
            print("Good! You guessed a letter.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")

    if '_' not in hiddenWord:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you're out of attempts. The word was: {word}")

play_hangman()

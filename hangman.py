import random

def hangman():
    words = ["apple", "banana", "orange", "grapes", "mango"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    print("🎯 Welcome to Hangman!")
    print("You have", attempts, "wrong attempts allowed.\n")

    while attempts > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.\n")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("✅ Good guess!\n")
        else:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts, "\n")

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("😢 Out of attempts! The word was:", word)

hangman()

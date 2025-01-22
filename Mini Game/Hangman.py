import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(words).lower()
    word_length = len(word)
    guessed_word = ['_'] * word_length
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good job! That letter is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

        if '_' not in guessed_word:
            print("\nCongratulations! You guessed the word correctly.")
            break
    else:
        print(f"\nGame over! The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    hangman()
import random

# Predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)
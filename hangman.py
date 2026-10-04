import random

# Words and clues
word_clues = {
    "python": "A programming language",
    "computer": "An electronic machine",
    "developer": "A person who creates software",
    "coding": "Writing programs",
    "keyboard": "Used to type on a computer"
}

# Hangman stages
hangman_stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

# Select random word
word = random.choice(list(word_clues.keys()))
clue = word_clues[word]

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("\n" + "=" * 40)
print("          HANGMAN GAME")
print("=" * 40)

print("\nCLUE:", clue)
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong_guesses:

    # Show hangman
    print(hangman_stages[wrong_guesses])

    # Show word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("WORD:", display)

    print("Guessed letters:", guessed_letters)

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 YOU WIN!")
        print("The word was:", word)
        break

    # Get guess
    guess = input("\nEnter a letter: ").lower()

    # Validate
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct!")

    # Wrong guess
    else:
        wrong_guesses += 1
        print("❌ Wrong!")
        print("Chances left:", max_wrong_guesses - wrong_guesses)

# Game over
if wrong_guesses == max_wrong_guesses:
    print(hangman_stages[wrong_guesses])
    print("\n💀 GAME OVER!")
    print("The correct word was:", word)

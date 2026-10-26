import random

# Step 1: Choose a random word
words = ["python", "apple", "school", "coding", "tiger"]
secret_word = random.choice(words)

# Step 2: Store guessed letters
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("      WELCOME TO HANGMAN!")
print("================================")

# Step 3: Start the game
while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Check if the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Get input from the player
    guess = input("Guess one letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Step 4: Show the final result
if all(letter in guessed_letters for letter in secret_word):
    print("You guessed the word:", secret_word)
else:
    print("\nGame over!")
    print("The correct word was:", secret_word)
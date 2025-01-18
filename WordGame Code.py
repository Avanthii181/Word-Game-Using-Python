import random  # Import the random module to select a random word

def display_word(word, guessed_letters):
    """
    Display the current state of the word with guessed letters revealed
    and unguessed letters replaced with underscores.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "developer", "keyboard", "function"]
    word = random.choice(words)  # Randomly select a word from the list
    guessed_letters = set()  # Set to store guessed letters
    attempts = 6  # Number of incorrect guesses allowed

    # Display a welcome message and the length of the word
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    # Main game loop
    while attempts > 0:
        # Display the word with guessed letters and underscores
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").lower().strip()

        # Validate input: Ensure it's a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1  # Reduce attempts for an incorrect guess

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        # If the player runs out of attempts, display the correct word
        print("\nYou ran out of attempts! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()  # Call the hangman function to start the game

# 📘 Assignment: Games in Python

## 🎯 Objective

Students will create a classic Hangman game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description

Create a Hangman game where the player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements

Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Display the current progress using underscores (e.g., `_ _ _ _ _`) updated after each correct guess
- Accept single-letter guesses from the player via user input
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display an appropriate win or lose message at the end

### 🛠️ Handle Invalid Input

#### Description

Add input validation to ensure the game handles unexpected or repeated guesses gracefully.

#### Requirements

Completed program should:

- Reject non-letter input and prompt the player to try again
- Notify the player if they guess a letter they have already tried
- Keep track of all previously guessed letters and display them each turn

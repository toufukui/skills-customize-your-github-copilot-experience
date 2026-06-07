
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that uses loops, conditionals, and string handling to let players guess a hidden word before their attempts run out.

## 📝 Tasks

### 🛠️ Build the game engine

#### Description
Create the core Hangman gameplay so the program can select a secret word, accept letter guesses, and show the player's current progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the player
- Display the current word state with unguessed letters hidden as `_`
- Track and update remaining attempts for incorrect guesses

### 🛠️ Add win/lose game flow

#### Description
Implement the game loop, ending conditions, and feedback messages so the player can win, lose, or continue guessing.

#### Requirements
Completed program should:

- Continue prompting until the word is guessed or attempts are exhausted
- End the game with a clear win or lose message
- Reveal the secret word when the player loses
- Show the player's progress and remaining attempts after each guess

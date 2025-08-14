import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(ascii_art.STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")
    return display_word.replace(" ", "")


def play_game():
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print(f"length of secret word: {len(secret_word)}")

    print("Welcome to Snowman Meltdown!")

    while True:
        display_word = display_game_state(mistakes, secret_word, guessed_letters)
        if display_word == secret_word:
            print("You won!")
            return
        print(f"solution word {display_word}")
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        print(f"mistakes: {mistakes}")        
        guessed_letters.append(guess)
        if not guess in secret_word:
            mistakes += 1
        if mistakes == len(STAGES):
            print("Game Over")
            return
        
    
if __name__ == "__main__":
    play_game()

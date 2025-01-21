import random

def scramble_word(word):
    """Scramble the letters of a word."""
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def play_game():
    """Main function to play the Word Scramble game."""
    words = ["python", "programming", "developer", "algorithm", "github", "computer", "keyboard", "software"]
    word = random.choice(words)
    scrambled_word = scramble_word(word)

    print("Welcome to Word Scramble!")
    print("Unscramble the word to win!")
    print(f"Scrambled word: {scrambled_word}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left.")
            else:
                print(f"Sorry, you're out of attempts. The correct word was: {word}")

if __name__ == "__main__":
    play_game()

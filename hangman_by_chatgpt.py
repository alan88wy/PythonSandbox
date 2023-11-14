import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    
    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! Attempts left: {max_attempts - attempts}")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts == max_attempts:
            print("Sorry, you ran out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()

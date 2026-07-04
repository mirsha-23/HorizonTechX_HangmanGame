import random

words = ["python", "computer", "hangman", "program", "developer"]

while True:
    secret_word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    print("\n===== HANGMAN GAME =====")

    while wrong_attempts < max_attempts:
        display = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("🎉 Congratulations! You guessed the word.")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single alphabet only.")
            continue

        if guess in guessed_letters:
            print("Letter already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_attempts += 1
            print("❌ Wrong guess.")
            print("Attempts left:", max_attempts - wrong_attempts)

    if wrong_attempts == max_attempts:
        print("\n💀 Game Over!")
        print("The word was:", secret_word)

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thank you for playing!")
        break
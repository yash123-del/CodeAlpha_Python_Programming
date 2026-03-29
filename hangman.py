import random

words = ["apple", "tiger", "chair", "house", "plant"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

guessed_letters = []

incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
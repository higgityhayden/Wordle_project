from english_words import get_english_words_set
import datetime

# Define a list of words to choose from
web2lowerset = get_english_words_set(['web2'], lower=True)

# Filter 5-letter words from the word list
five_letter_words = [word for word in web2lowerset if len(word) == 5]

# Get the current day of the year (1 to 365)
day_of_year = datetime.date.today().timetuple().tm_yday

# Calculate the index for the word of the day
word_index = day_of_year % len(five_letter_words)

# Get the word of the day
word_of_the_day = five_letter_words[word_index]


# Function to evaluate the user's input
def evaluate_guess(secret_word, guess):
    result = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result.append("Match")
        elif guess[i] in secret_word:
            result.append("Close Match")
        else:
            result.append("No Match")
    return result


#Function to execute program
def play_wordle():
    secret_word = word_of_the_day
    attempts = 0

    print("Welcome to Wordle!")
    print("You have 6 attempts to guess a five-letter word.")

    while attempts < 6:
        guess = input(f"Attempt {attempts + 1}: ").lower()
        while guess not in five_letter_words:
            print("Please enter a five-letter word")
            guess = input(f"Attempt {attempts + 1}: ").lower()

        if guess == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

        feedback = evaluate_guess(secret_word, guess)
        print("Feedback:")
        for letter, color in zip(guess, feedback):
            print(f"{letter}: {color}")

        attempts += 1

    if attempts == 6:
        print(f"Sorry, you've used all your attempts. The word was: {secret_word}")


if __name__ == "__main__":
    play_wordle()

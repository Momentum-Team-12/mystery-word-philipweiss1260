 # validates guess
import random


def play_game(file):
    with open('words.txt') as f:
        file_string = f.read().lower()
        file_list = file_string.split()
        random_word = random.choice(file_list)
        print(random_word)
    
        print(f"Word length is {len(random_word)}.")
        file_string = file_string.lower()
    # above makes uppercase letters for visibility purpose
    # below makes characters of word into list
        # word_list = file_string.split()
        # print(word_list)
    chance = 8
    guesses = []

    while True:
        guess = input("Please guess a letter: ").lower()
        
        # print(guess)
        incomplete = 0
        if guess in guesses:
            print(f"Whoops you already guessed {guess}.")
        elif guess in random_word:
            print(guess)
            guesses.append(guess)
            for letter in random_word:
                if letter in guesses:
                    print(letter, end=' ')
                else:
                    incomplete += 1
                    print("_ ", end=' ')
            print("You guessed correctly.")
            if incomplete == 0:
                print("Congratulations, you won, the word is:", random_word)
                break
        elif guess not in random_word:
            if guess in guesses:
                print(f"Whoops you already guessed {guess}.")
            elif guess not in guesses:
                guesses.append(guess)
                chance -= 1
                print(f"Sorry, try again, you have {chance} chances left.")
            if chance == 0:
                print("You have run out of guesses, the word is:", random_word)
                break
    # then check guess against word's letters
    # tell user if guess is in word
    # user can then guess again


if __name__ == "__main__":
    play_game('words.txt')
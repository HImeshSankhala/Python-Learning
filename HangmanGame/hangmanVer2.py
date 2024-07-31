import random
from collections import Counter
import threading
import time
import sys

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

def countdown_timer(timeout, stop_event):
    for remaining in range(timeout, 0, -1):
        if stop_event.is_set():
            return
        sys.stdout.write(f'\rTime left: {remaining} seconds             ')
        sys.stdout.flush()
        time.sleep(1)
    if not stop_event.is_set():
        sys.stdout.write('\rTime is up!              \n')
        sys.stdout.flush()
        stop_event.set()

def input_with_timeout(prompt, timeout):
    guess = ''
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=countdown_timer, args=(timeout, stop_event))
    timer_thread.start()
    try:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        guess = input()
        stop_event.set()
        timer_thread.join()  # wait for the timer thread to finish
    except EOFError:
        guess = ''
    except KeyboardInterrupt:
        sys.stdout.write('\nGame interrupted. Exiting...\n')
        sys.stdout.flush()
        exit()
    return guess, stop_event.is_set()

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: # flag is updated when the word is correctly guessed
            print()
            print(f'You have {chances} chances left.')  # Display remaining chances

            guess, time_up = input_with_timeout('\t\tEnter a letter to guess: ', 10)  # 10-second timer for each guess

            if time_up and not guess:  # Only conclude game if time ran out without a guess
                chances = 0  # Set chances to 0 to trigger the losing condition
                break  # Exit the loop if time is up

            chances -= 1

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess # The guess letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    print("\nThe word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break # To break out of the for loop and while loop
                else:
                    print('_', end=' ')
            print()  # Added to ensure new lines between each attempt

        # If user has used all of his chances or time is up
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

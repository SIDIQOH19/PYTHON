# A word guessing game

import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += '_'
print(placeholder)

game_over = False
correct_letters = []


while not game_over:
    print(f'****{lives}/6 LIVES LEFT****')
    guess = input('Guess a letter: ').lower()
    display = ''
    for char in chosen_word:
        if guess == char:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += '_'
    print('Word to guess:', display)

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that is not the word. You lose a life')

        if lives == 0:
            game_over = True
            print(f'The word is {chosen_word}. You LOSE')

    if "_" not in display:
        game_over = True
        print("You WIN.")

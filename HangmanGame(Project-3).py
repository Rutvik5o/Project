#Project: Hangman Game ~Rutvik50


import random
import hangman_stages
import wordfileby50


lives=6
chosen_word=random.choice(wordfileby50.words)

#print(chosen_word)

display=[]

for i in range(len(chosen_word)): # 1 2 3 4 5  Apple
    display += '_'

print(display)

game_over=False

while not game_over:

    guessed_letter=input("Guess a letter").lower() #x_ _ _ _ _

    for position in range(len(chosen_word)): # 0 1 2 3 4

        letter=chosen_word[position]

        if letter ==guessed_letter: # p==x

            display[position]=guessed_letter

    print(display)

    if guessed_letter not in chosen_word:

            lives -=1

            if lives == 0:

                game_over=True

                print("Your Loose!")

    if '_'  not in display:

            game_over=True

            print("You Win!")

    print(hangman_stages.stages[lives])

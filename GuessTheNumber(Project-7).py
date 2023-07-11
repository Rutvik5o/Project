# Guess The Number -> Project 7

import random
import Art


Easy_level_attempts=10

Hard_level_attempts=5

def set_difficulty(level_chosen):

    if level_chosen=="easy":
        return Easy_level_attempts

    elif level_chosen=="hard":
        return Hard_level_attempts

    else:
        return

def check_answer(gussed_number,answer,attempts):

    if gussed_number<answer:

         print("You Guess Is Too Low ＞﹏＜")

         return attempts-1

    elif gussed_number>answer:

        print("Your Guess Is Too High ⊙﹏⊙∥" )

        return attempts-1


    else:

        print(f"Your Guess is Right (*^▽^*) The answer was -> {answer}")


def game():

    print(Art.logo)

    print("Let me think 🤔 of a number between 1 to 50")

    answer=random.randint(1,50)

    level=input("Chosen level of difficulty \n->Type 'Easy'\nor\n->Type 'Hard'😁").lower()

    attempts=set_difficulty(level)

    if attempts!= Easy_level_attempts and attempts!= Hard_level_attempts:

        print("You have entered wrong difficulty level... ^_^  Play Again!")

        return

    gussed_number=0

    while gussed_number!=answer:

        print(f"You have {attempts} attempts remaining to guess the number")

        gussed_number=int(input("Guess a Number (●'◡'●) ->"))

        attempts=check_answer(gussed_number,answer,attempts)

        if attempts == 0:

            print("You have out of gussess ￣へ￣ You Losses")

            return

        elif gussed_number!=answer:

            print("Guess Again 😉")


game()
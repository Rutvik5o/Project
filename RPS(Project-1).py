import random
rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

 '''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


games_images=[rock,paper,scissors]

user_choice=int(input("Enter Your choice:\nType->\nFor Rock:0\nFor Paper:1\nFor Scissors=2"))

if user_choice >= 3 or user_choice <0:

    print("You Entered Invalid Number")

else:

    print(games_images[user_choice])

    computer_choice=random.randint(0,2)

    print("Computer Choose:")

    print(games_images[computer_choice])


    if computer_choice == user_choice:

        print("Hey, It's a draw.")

    elif computer_choice == 0 and user_choice == 2:

        print("You Lose.")

    elif user_choice == 0 and computer_choice == 2:

        print("You Win.")

    elif computer_choice > user_choice:

        print("You Lose.")

    elif computer_choice > computer_choice:

        print("You win.")
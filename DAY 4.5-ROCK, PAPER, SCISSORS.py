# To play a game of Rock, Paer, and Scissors.
import random
print('Welcome to a game of Rock, Paper, Scissors')
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
---'   ____)____
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
my_choice = int(
    input('What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

computer_choice = random.randint(0, 2)

print(f'Computer Chose: {computer_choice}')

if my_choice == 1 and computer_choice == 2:
    print('You win!')
elif my_choice == 2 and computer_choice == 0:
    print('Computer wins!')
elif my_choice == 1 and computer_choice == 2:
    print('Computer wins!')
else:
    print('Emapami')
will come back to this

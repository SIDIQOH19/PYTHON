print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to the Treasure Island.')
print('Your mission is to find the treasure!')
direction = input(
    'You are at a crossroad. Where do do want to go?' "Type 'left' to go left and type 'right' to go right\n")
if direction == 'left':
    action = input(
        'You are at a lake and there are two options.' "Type 'wait' to wait for a boat and 'swim' to swim across the lake\n")
    if action == 'wait':
        door_colour = input(
            'This is the final stage and you have to pick the right door.' "Type 'blue' or 'yellow' or 'red' to pick\n")
        if door_colour == 'yellow':
            print('You win!!!')
        else:
            print('Aww, you picked the wrong door. Please try again')
    else:
        print('You drowned while swimming. Game over!')
else:
    print('Oops , you fell. Game over!.')

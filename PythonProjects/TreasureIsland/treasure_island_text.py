import time

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

def print_slowly(text, delay = 0.07):
    for char in text:
        print(char, end = '', flush = True)
        time.sleep(delay)
    print()

prompt_a = input("\nYou find yourself standing at the entrance of the dark and mysterious dungeons of Treasure Island. There are two paths ahead of you. Will you choose to go 'left' or 'right'? Choose wisely!\n ")
prompt_a_lower = prompt_a.lower()

if prompt_a_lower == "left":
    print("You have fallen into the pit trap! Game over.")
    exit() # Game ends if user chooses left path
elif prompt_a_lower == "right":
    print("You continue along the 'right' path. 😏")
    print("\nYou cautiously proceed down the path you've chosen and arrive at a chamber with three doors. Each door seems to have its secret.")
    while True:
        prompt_b = input("Will you open the 'left' door, the 'middle' door, or the 'right' door?\n ")
        prompt_b_lower = prompt_b.lower()

        if prompt_b_lower == "left":
            print("You open the left door, but it's just a solid wall. Try another.")
            
        elif prompt_b_lower == "middle":
            print("You carefully open the middle door and find another passage to explore.")
            break

        elif prompt_b_lower == "right":
            print("You triggered a booby trap. Game over.")
            exit()
        else:
            print("Invalid input. Please choose 'left', 'middle', or 'right' when selecting the door.")

prompt_c = input("\nAs you step forward, you trigger an ancient arrow trap! Arrows are flying towards you! Will you 'jump' to dodge them or 'duck' to avoid getting hit?\n ")
prompt_c_lower = prompt_c.lower()

if prompt_c_lower == "duck":
    print("Good choice! You successfully avoid the arrows and move forward.\n")
    time.sleep(2)
    print_slowly("\nCongratulations! You made it past the arrow trap and continue deeper into the dungeos. After a few moments of walking, you see a glimmer of light ahead. And there it is, the legendary treasure chest of Treasure Island, right in front of you! You found the lost treasure!", delay = 0.03)
elif prompt_c_lower == "jump":
    print("Your jump was not high enough to avoid the arrows. The game lobby awaits you.")
    exit()
else: 
    print("Invalid input. Please choose 'duck', or 'jump'.")
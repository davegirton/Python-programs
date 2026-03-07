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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

input("When you are ready type: start. ")

print("You have come to a crossroad and must choose 'left' or 'right'.")
cross_road_choice = input("What is your choice: ")
if cross_road_choice == "left":
    print("Great, you are on the correct path.")

    print("If front of you is a body of water with an island in the middle. Do you wait for a boat or swim?")
    water_option = input("What is your choice: 'wait' or 'swin' ")
    if water_option == "wait":
        print("Good option. You have made it to the island.")

        print("Now you are looking at 3 doors. 1 red, 1 blue, 1 green. You must choose which to open.")
        doors = input("What is your choice: 'red', 'blue', 'green' ")
        if doors == "red":
            print("You die by fire. GAME OVER.")
        elif doors == "blue":
            print("You find the treasure sitting on a cloud. YOU WIN!!!")
        else:
            print("A dinosaur eats you. GAME OVER.")
    else:
        print("A shark has eaten you. GAME OVER.")
else:
    print("You fell into a trap and died.")
    print("Game Over.")

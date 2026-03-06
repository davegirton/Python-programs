print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"A childs ticket is ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"A young adult ticket is ${bill}.")
    else:
        bill = 12
        print(f"An adult ticket is ${bill}.")

    photo_choice = input("Would you also like a photo for $3? Type y for YES and n for NO: ")
    if photo_choice == "y":
        bill += 3
    print(f"Your total bill is ${bill:.2f}")
else:
    print("Sorry you have to grow taller before you can ride.")

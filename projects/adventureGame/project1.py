name = input("What is your name? ")
print("Hello", name, "Welcome to the world of Drox")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("Let your adventure begin!")
    weapon = input("Choose a weapon (sword/axe)")

    direction = input("What direction do you wish to go? (Left/Right) ").lower()
    if direction == "left":
        print("You advance to the left")
    elif direction == "right":
        print("You advance to the right")
        choice = input("You now stopped in front of a bridge, do you want to cross or swim pass the river?")
        if choice == "cross" and weapon == "axe":
            print("You cross the bridge safely")
        else:
            print("You swim pass the river and get eaten by a giant Salmon.")
            print("Game over, you died")
    else:
        print("You encounter a deadly Gnoll")
        print("Game over, You died")

else:
    print("I wish you the best of luck adventurer")



# Text-Based Adventure Game Code with Comments

# Get the player's name
name = input("What is your name? ")
print("Hello", name, "Welcome to the world of Drox")

# Ask if the player wants to play
should_we_play = input("Do you want to play? ").lower()

# Check if the player wants to play
if should_we_play == "yes" or should_we_play == "y":
    print("Let your adventure begin!")

    # Let the player choose a weapon
    weapon = input("Choose a weapon (sword/axe)")

    # Ask the player which direction they want to go
    direction = input("What direction do you wish to go? (Left/Right) ").lower()
    if direction == "left":
        # Player chooses to go left
        print("You advance to the left")
    elif direction == "right":
        # Player chooses to go right
        print("You advance to the right")
        # Player encounters a bridge and must make a choice
        choice = input("You now stopped in front of a bridge, do you want to cross or swim pass the river?")
        if choice == "cross" and weapon == "axe":
            # Player safely crosses the bridge if they have an axe
            print("You cross the bridge safely")
        else:
            # Player tries to swim and is eaten by a giant Salmon
            print("You swim pass the river and get eaten by a giant Salmon.")
            print("Game over, you died")
    else:
        # Player chooses an invalid direction and encounters a deadly Gnoll
        print("You encounter a deadly Gnoll")
        print("Game over, You died")

else:
    # Player chooses not to play
    print("I wish you the best of luck adventurer")

# Comments for Future Improvement:
# - Add input validation to ensure player enters valid options (e.g., yes/no, left/right).
# - Modularize the code into functions like start_game(), choose_weapon(), choose_direction(), etc.
# - Add a replay option for the player to restart after game over.
# - Use loops to handle invalid input until a correct choice is provided.

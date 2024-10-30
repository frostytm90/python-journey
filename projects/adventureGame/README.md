# Text-Based Adventure Game

Welcome to **Drox**, a simple text-based adventure game written in Python. This project is part of my Python learning journey and demonstrates the basics of user input, decision making, and conditional statements.

## Overview
This is an interactive text-based adventure game where players make choices to progress in the story. The choices you make affect your journey and can determine your survival. You start by entering your name, choosing a weapon, and navigating through different scenarios.

## Key Features
- **User Input**: Players enter their name and make decisions about their journey.
- **Choices and Outcomes**: The player makes choices that impact how the story unfolds.
- **Simple Combat**: Players select a weapon and make choices that affect their survival.

## Motivation
I created this project to learn how to use Python for creating interactive command-line experiences. It was a fun way to apply basic programming concepts, such as variables, conditionals, and user inputs.

## Technologies Used
- **Python**: This game is written in Python, making use of standard input/output to create an interactive experience.

## Installation Instructions
1. **Clone the Repository**: Download or clone the repository to your local machine.
   ```
   git clone https://github.com/frostytm90/python-journey.git
   ```
2. **Run the Script**: Open your terminal and run the Python script.
   ```
   python textBaseAdventureGame.py
   ```

## How to Play
1. Enter your name to start the adventure.
2. Choose whether or not you want to play.
3. Select your weapon (**sword** or **axe**).
4. Make choices about which direction to go and how to handle obstacles.
5. Your choices determine whether you survive or not!

## Possible Areas for Improvement
- **More Branching Paths**: Currently, the game has limited branching options. Adding more paths and outcomes would make the game richer.
- **Combat System**: Implementing a simple combat system with random chances to win could make the game more interesting.
- **Inventory System**: Adding an inventory to allow players to collect items could increase the depth of the game.
- **Saving Progress**: Allow players to save and load their progress for a more immersive experience.

## Future Improvements
I plan to add more complexity to the game, such as:
- Adding multiple weapons and enemies.
- Creating more choices that can lead to different endings.
- Enhancing the story with more detailed descriptions and richer branching.

## Comments and Areas for Improvement in Code
- **Input Validation**: It would be great to validate user inputs to avoid unexpected responses.
- **Modularization**: Break down the game into functions like `start_game()`, `choose_weapon()`, etc., to make the code more readable.
- **Replay Option**: Add an option for the player to replay after the game ends.
- **Loop for Valid Choices**: Use a loop to prompt the player until they provide valid input (e.g., valid direction or weapon choice).

Feel free to contribute or provide feedback on how to improve this game!


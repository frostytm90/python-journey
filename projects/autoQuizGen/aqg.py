import random
import json
import time

# Function to load questions from the JSON file
def load_questions():
    # Open and read the "questions.json" file
    with open("questions.json", "r") as f:
        # Load the "questions" list from the JSON file
        questions = json.load(f)["questions"]
    return questions

# Function to get a specified number of random questions from the list
def get_random_questions(questions, num_questions):
    # Ensure that the number of questions requested does not exceed the total available
    if num_questions > len(questions):
        num_questions = len(questions)
    
    # Randomly select the requested number of questions
    random_questions = random.sample(questions, num_questions)
    return random_questions

# Function to ask a question to the user and return whether the answer is correct or not
def ask_question(question):
    # Display the question text
    print(question["question"])
    
    # Display each option with a number (e.g. 1. Option A)
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    # Get the user's answer as an integer input
    user_input = int(input("Enter your answer: "))
    
    # Check if the input is within the valid range of options
    if user_input < 1 or user_input > len(question["options"]):
        print("Wrong Answer.")
        return False
    
    # Check if the selected option is the correct answer
    correct = question["options"][user_input - 1] == question["answer"]
    return correct

# Load all questions from the JSON file
questions = load_questions()

# Ask the user how many questions they want to answer
total_questions = int(input("Enter the number of questions: "))

# Get the specified number of random questions to ask the user
random_questions = get_random_questions(questions, total_questions)

# Initialize the correct answer count
correct = 0
# Start timing the quiz
start_time = time.time()

# Loop through each randomly selected question
for question in random_questions:
    # Ask the question and check if the answer is correct
    is_correct = ask_question(question)
    if is_correct:
        correct += 1  # Increment the correct answer count if the answer is right
    
    # Display a separator line between questions
    print("--------------------------------")

# Display the summary of the quiz
completion = time.time() - start_time  # Calculate the total time taken
print("Summary")
print("Total Questions:", total_questions)
print("Correct Answer:", correct)
print(f"Score: {(correct / total_questions) * 100}%")  # Calculate and display the score percentage
print("Time Taken:", round(completion, 2), "seconds")

# Add more questions as needed
# Each question should have 4 options and only one correct answer
# The options should be randomly ordered
# The questions should be stored in a JSON file for easy access
# The JSON file should be updated when a new question is added or the answer is updated

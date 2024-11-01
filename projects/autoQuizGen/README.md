# Quiz Game

This is a Python-based quiz game that allows users to answer multiple-choice questions. The questions are loaded from a JSON file, and the user can specify the number of questions they want to answer.

## Features
- Loads questions from a JSON file (`questions.json`).
- Allows the user to specify how many questions they want to answer.
- Displays multiple-choice questions and records user responses.
- Provides a summary of the quiz, including total questions, correct answers, score, and time taken.

## How to Use
1. **Prepare the JSON File**: Create a JSON file named `questions.json` that contains the questions in the following format:
   ```json
   {
     "questions": [
       {
         "question": "What is the capital of France?",
         "options": ["Berlin", "Madrid", "Paris", "Rome"],
         "answer": "Paris"
       },
       {
         "question": "Which planet is known as the Red Planet?",
         "options": ["Earth", "Mars", "Jupiter", "Venus"],
         "answer": "Mars"
       }
     ]
   }
   ```
   Make sure each question has exactly one correct answer, and each question contains four options.

2. **Run the Script**: Execute the Python script:
   ```sh
   python quiz_game.py
   ```

3. **Answer Questions**: The script will prompt you to enter the number of questions you want to answer and then display each question one by one. Enter the number corresponding to your answer.

4. **View the Summary**: After completing the quiz, the script will display a summary with your score and the time taken to complete the quiz.

## Requirements
- Python 3

## Example
1. Run the script.
2. Enter the number of questions you want to answer (e.g., `2`).
3. Answer each question by entering the number corresponding to the correct answer.
4. The script will display a summary like:
   ```
   Summary
   Total Questions: 2
   Correct Answer: 1
   Score: 50.0%
   Time Taken: 12.34 seconds
   ```

## Notes
- If the user enters an invalid option, the answer will be marked as incorrect.
- The `questions.json` file should be updated with new questions when needed.

## Future Improvements
- Add support for tracking user scores over multiple quizzes.
- Include more detailed feedback for incorrect answers.
- Implement a graphical user interface (GUI) for a better user experience.


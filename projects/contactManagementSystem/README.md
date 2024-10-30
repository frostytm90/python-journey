# Contact Management System

Welcome to the **Contact Management System**, a simple command-line Python application for managing contact information. This project is part of my Python learning journey and helps to understand data storage, user input handling, and file operations.

## Overview
The Contact Management System allows users to add, delete, search, and manage contacts. Each contact includes basic details such as name, age, and email address. The data is stored in a JSON file for persistence between sessions.

## Key Features
- **Add Contact**: Allows users to add new contacts with name, age, and email.
- **Delete Contact**: Users can delete a specific contact by selecting it from the list.
- **Search Contacts**: Users can search for a contact by name.
- **Persistent Storage**: Contacts are saved to a JSON file, allowing the user to retrieve the data even after closing the application.

## Motivation
This project was created to practice working with file operations, lists, and dictionaries in Python, as well as to handle user input effectively. It was a good exercise to explore how to manage data persistence using JSON.

## Technologies Used
- **Python**: The program is implemented in Python, using the `json` library for data storage and retrieval.

## Installation Instructions
1. **Clone the Repository**: Download or clone the repository to your local machine.
   ```
   git clone https://github.com/frostytm90/python-journey.git
   ```
2. **Run the Script**: Open your terminal and run the Python script.
   ```
   python contact_management_system.py
   ```

## How to Use
1. **Load Contacts**: The app automatically loads existing contacts from the `contacts.json` file.
2. **Add a Contact**: Enter the details when prompted to add a new contact.
3. **Delete a Contact**: Display the contact list and choose a contact to delete by number.
4. **Search Contacts**: Enter a name to search and display matching contacts.
5. **Exit**: Type `exit` to close the application, and all contact changes will be saved.

## Possible Areas for Improvement
- **Input Validation**: Validate email format to ensure users provide valid email addresses.
- **Edit Contact**: Add functionality to edit existing contact details.
- **Improved Error Handling**: Handle issues like missing JSON files or corrupted data more gracefully.
- **Confirmation for Deletion**: Add a confirmation step before deleting a contact to avoid accidental deletions.
- **Modularization**: Separate contact loading and saving into dedicated functions for improved code readability.

## Future Improvements
I plan to enhance the system by:
- Adding more input validation, especially for email addresses.
- Allowing users to edit existing contacts.
- Implementing a graphical user interface (GUI) for a more user-friendly experience.
- Adding support for phone numbers and address fields for each contact.

## Comments and Areas for Improvement in Code
- **Modularization**: Refactor the code to move file operations to separate functions.
- **Validation**: Improve the validation for inputs, such as ensuring that the email has a valid format.
- **User Experience**: Add confirmation messages for deleting contacts to improve user experience and avoid errors.
- **Exception Handling**: Add exception handling for JSON file operations to ensure robustness.

Feel free to contribute or provide feedback on how to improve the system!

## License
This project is open-source and available under the [MIT License](LICENSE).


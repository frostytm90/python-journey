# Contact Management System Code with Comments

import json

# Function to add a new contact
def add_person():
    # Get contact details from the user
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    # Create a dictionary to store the contact information
    person = {
        "name": name,
        "age": int(age),  # Convert age to an integer
        "email": email
    }
    return person

# Function to display all contacts
def display_people(people):
    # Iterate over the list of people and display their information
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

# Function to delete a contact
def delete_contact(people):
    # Display all contacts to the user
    display_people(people)

    while True:
        # Get the number of the contact to delete
        number = input("Select a number to delete: ")
        try:
            number = int(number)
            # Check if the number is valid
            if number <= 0 or number > len(people):
                print("Number you are trying to delete is invalid")
            else:
                break
        except:
            # Handle invalid input that cannot be converted to an integer
            print("Number you are trying to delete is invalid")

    # Remove the selected contact from the list
    people.pop(number - 1)
    print("Person details deleted successfully.")

# Function to search for a contact by name
def search(people):
    # Get the search term from the user
    search_name = input("Search for a name: ").lower()
    results = []

    # Iterate over the contacts and add matches to the results list
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    
    # Display the search results
    display_people(results)

# Welcome message for the user
print("Hello there! Welcome to the Contact Management System.")
print()

# Load the contacts from the JSON file
with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

# Main program loop
while True:
    print()
    # Display the size of the contact list and prompt the user for a command
    print("Contact list size: ", len(people))
    command = input("You can 'Add', 'Delete/Remove' or 'Search' and 'Exit' to close: ").lower()

    # Handle the user's command
    if command == 'add':
        # Add a new contact
        person = add_person()
        people.append(person)
        print("Person added successfully")
    elif command == 'delete':
        # Delete a contact
        delete_contact(people)
    elif command == 'search':
        # Search for a contact
        search(people)
    elif command == 'exit':
        # Exit the program
        break
    else:
        # Handle invalid commands
        print("Invalid command")

    # Print the current list of contacts
    print(people)

# Save the updated contact list to the JSON file
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)

# Comments for Future Improvement:
# - Add input validation for email format to ensure valid email addresses.
# - Modularize the code further by creating separate functions for loading and saving contacts.
# - Improve error handling for the JSON file operations (e.g., handle missing or corrupted files).
# - Allow for editing contact details, not just adding or deleting.
# - Add a feature to confirm before deleting a contact to prevent accidental deletions.

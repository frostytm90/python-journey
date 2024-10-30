import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name": name,
        "age": int(age),
        "email": email
    }
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Select a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Number you are trying to delete is invalid")
            else:
                break
        except:
            print("Number you are trying to delete is invalid")

    people.pop(number - 1)
    print("Person details deleted successfully.")


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    
    display_people(results)

print("Hello there! Welcome to the Contact Management System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list size: ", len(people))
    command = input("You can 'Add', 'Delete/Remove' or 'Search' and 'Exit' to close: ").lower()

    if command == 'add':
        person = add_person()
        people.append(person)
        print("Person added successfully")
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search(people)
    elif command == 'exit':
        break
    else:
        print("Invalid command")

    print(people)

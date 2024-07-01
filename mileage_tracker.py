import json
import pandas as pd 
from termcolor import colored


def load_data():
    try:
        with open('shoe_database.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError: # use of error handling except 
        data = {} #json structure is dictionary
    return data

def load_data_from_json(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = [] 
    return data

def save_data(data):
    with open('shoe_database.json', 'w') as f:
        json.dump(data, f, indent=4)

def add_run(data, shoe_name, distance):
    if shoe_name in data:
        data[shoe_name] += distance
    else:
        data[shoe_name] = distance

def add_new_shoe(data, shoe_name):
    data[shoe_name] = 0  # Assuming initial km's is 0
    save_data(data)      # Save updated data to the JSON file


def view_shoe_mileage(file_name):
    # Load shoe data from JSON
    shoe_data = load_data_from_json(file_name)

    if not shoe_data:
        print("No shoes tracked yet.")
        return

    # Print header
    print(colored("Shoe Mileage Tracker", 'green'))
    print(colored("--------------------", 'green'))


    # Print out each shoe's details
    for shoe in shoe_data:
        shoe_model = shoe.get('Shoe Model', 'Unknown Model')
        total_mileage = shoe.get('Total Mileage', 'Unknown Mileage')
         # Print that shoes details in pink
        print(colored(f"{shoe_model}: {total_mileage} kilometers", 'blue'))


# Example to use:
# file_name = 'shoe_database.json'
# view_shoe_mileage(file_name)

def delete_shoe(data, shoe_name):
    if shoe_name in data:
       del data[shoe_name]

def check_shoe_reminders(data, mileage_threshold=800):
    reminders = []
    for shoe_name, shoe_info in data.items():
        total_mileage = shoe_info.get('Total Mileage', 0)
        if total_mileage >= mileage_threshold:
            reminders.append(f"Reminder: Shoe '{shoe_name}' has reached {mileage_threshold} kilometers.")

    return reminders

def main():
    data = load_data()
    print(data)
    while True:
        print(colored("\nShoe Mileage Tracker", 'white'))
        print(colored("1. Add Run", 'magenta'))
        print(colored("2. View Shoe Mileage", 'yellow'))
        print(colored("3. Add New Shoe", 'blue'))
        print(colored("4. Delete Shoe", 'red'))
        print(colored("5. Check Reminders", 'yellow'))
        print(colored("5. Exit", 'green'))
        choice = input(colored("What would you like to do? ", 'white'))
        
        if choice == '1':
            shoe_name = input("Enter shoe name: ")
            distance = float(input("What distance did you run (in km's): "))
            add_run(data, shoe_name, distance)
            print("Run added!")
        elif choice == '2':
            print("\nShoe Mileage:")
            for shoe, mileage in data.items():
                print(f"{shoe}: {mileage} miles")
        elif choice == '3':
            shoe_name = input("Enter new shoe name: ")
            add_new_shoe(data, shoe_name)
            print(f"Shoe '{shoe_name}' added!")
        elif choice == '4':
            shoe_name = input("Enter the shoe you would like to delete: ")
            delete_shoe(data, shoe_name)
            print(f"Shoe '{shoe_name}' deleted!")
        elif choice == '5':
            save_data(data)
            print(colored("Exiting program. See ya later!", 'magenta'))
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()

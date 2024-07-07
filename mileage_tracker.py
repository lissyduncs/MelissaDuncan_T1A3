import json
import pandas as pd 
from termcolor import colored


def load_data():
    try: #use of try/except
        with open('shoe_database.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError: 
        data = {} 
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
        print(colored("Run added!", 'green'))
    else:
        data[shoe_name] = distance
        print(colored("New shoe added!", 'green'))

    save_data(data)




#def add_run(data, shoe_name, distance):
   # if shoe_name in data:
       # data[shoe_name] += distance
        #print(colored("Run added!", 'green'))
    #else:
       # print(colored("Shoe not found in database.", 'red'))

    
    #else:
        #data[shoe_name] = distance

def add_new_shoe(data, shoe_name):
    data[shoe_name] = 0  #  initial km's is 0
    save_data(data)      # Save updated data to  JSON file


def view_shoe_mileage(file_name):
    
    shoe_data = load_data_from_json(file_name)

    if not shoe_data:
        print("No shoes tracked yet.")
        return

    # Print header
    #print(colored("Shoe Mileage Tracker", 'green'))
    #print(colored("--------------------", 'green'))


    # Print out each shoe's details
    for shoe in shoe_data:
        shoe_model = shoe.get('Shoe Model', 'Unknown Model')
        total_mileage = shoe.get('Total Mileage', 'Unknown Mileage')
         # Print that shoes details in pink
        print(colored(f"{shoe_model}: {total_mileage} kilometers", 'blue'))


def delete_shoe(data, shoe_name):
    if shoe_name in data:
       del data[shoe_name]


def main():
    data = load_data()
    shoe_name = "" # initalise it
    
    while True:
      # Display the menu options in colored text
        print(colored("\nWelcome to the Shoe Mileage Tracker", 'yellow'))
        print(colored("1. Add Run km's to shoe", 'magenta'))
        print(colored("2. View Shoe Mileage", 'magenta'))
        print(colored("3. Add New Shoe", 'magenta'))
        print(colored("4. Delete Shoe", 'magenta'))
        print(colored("5. Exit", 'blue'))
        choice = input(colored("What would you like to do? ", 'green'))
        
        if choice == '1':
            shoe_name = input(colored("Enter shoe name: ", 'blue'))
    
            while True:
                try:
                    distance = float(input("What distance did you run (in km's): "))
                    break  
                except ValueError:
                    print(colored("Invalid distance. Please enter a valid number.", 'red'))

            add_run(data, shoe_name, distance)

 
            if data.get(shoe_name, 0) >= 800:
                 print(colored("It's time for you to get new shoes!", 'red'))
    
            print(colored("Run added!", 'green'))  # Print "Run added!" message after successful addition


        elif choice == '2':
            if not data:  # Check if the data is empty
                print(colored("No shoes tracked yet.", 'yellow'))
            print("\nShoe Mileage:")
            for shoe, mileage in data.items():
                print(f"{shoe}: {mileage} km's")
        elif choice == '3':
            shoe_name = input("Enter new shoe name: ")
            add_new_shoe(data, shoe_name)
            print(colored(f"Shoe '{shoe_name}' added!", 'green'))
        elif choice == '4':
            shoe_name = input("Enter the shoe you would like to delete: ")
            delete_shoe(data, shoe_name)
            print(colored(f"Shoe '{shoe_name}' deleted!", 'red'))

        elif choice == '5':
            save_data(data)
            print(colored("Exiting program. See ya later!", 'magenta'))
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()

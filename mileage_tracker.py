import json
import pandas as pd 

def load_data():
    try:
        with open('shoe_database.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
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
    data[shoe_name] = 0  # Assuming initial mileage is 0
    save_data(data)      # Save updated data to the JSON file


def view_shoe_mileage(data):
    if not data:
        print("No shoes tracked yet.")
        return

    # Using pandas DataFrame for easier manipulation (optional)
    df = pd.DataFrame(list(data.items()), columns=['Shoe', 'Mileage'])
    print("Shoe Mileage Tracker")
    print(df.to_string(index=False))

# Call the function to view shoe mileage
view_shoe_mileage(shoe_data)



def delete_shoe(data, shoe_name):
    if shoe_name in data:
        del data[shoe_name]

def main():
    data = load_data()
    while True:
        print("\nShoe Mileage Tracker")
        print("1. Add Run")
        print("2. View Shoe Mileage")
        print("3. Add New Shoe")
        print("4. Delete Shoe")
        print("5. Exit")
        choice = input("What would you like to do? ")
        
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
            shoe_name = input("Enter shoe name to delete: ")
            delete_shoe(data, shoe_name)
            print(f"Shoe '{shoe_name}' deleted!")
        elif choice == '5':
            save_data(data)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()

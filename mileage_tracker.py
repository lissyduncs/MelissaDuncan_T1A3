import json
import os

DATA_FILE = 'data/shoe_database.json'

def add_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_run(data, shoe_name, distance):
    if shoe_name not in data:
        data[shoe_name] = 0
    data[shoe_name] += distance
    save_data(data)

def main():
    data = load_data()
    while True:
        print("\nShoe Mileage Tracker")
        print("1. Add Run")
        print("2. View Mileage")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            shoe_name = input("Enter shoe name: ")
            distance = float(input("Enter distance (in miles): "))
            add_run(data, shoe_name, distance)
            print("Run added!")
        elif choice == '2':
            for shoe, mileage in data.items():
                print(f"{shoe}: {mileage} miles")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

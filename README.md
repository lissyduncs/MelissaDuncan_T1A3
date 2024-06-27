# MelissaDuncan_T1A3
## Overview

The Shoe Mileage Tracker is a terminal application using Python, which is designed to help runners track how many kilometers they have run in their shoes. It can be hard to track how much running has been done in any particular pair of shoes (particularly when you have multiple on the go at the one time)The shoe mileage tracker provides a user-friendly interface to add new runs to each shoe, view selected shoe mileage, manage multiple shoes, and ensuring the data is stored.
The Shoe Mileage Tracker is an essential app for runners to track shoe usage and make informed decisions about replacing theor shoes in order to prevent injuries from wearing old footwear.

# Key Features:
- Add Runs: User can log runs in kilometers and assigns that to specific shoe. 
- View Shoe Mileage**: See accumulated mileage for each shoe.
- Add and Delete Shoes: User can add other shoes when they get a new pair as well as delete old ones that they no longer need

- Data Storage: All data is stored in `shoe_database.json`, ensuring the data is accessible and saved correctly.


## Installation

1. Clone the repository: https://github.com/lissyduncs/MelissaDuncan_T1A3

2. Install packages: pip install pandas
pip install -r requirements.txt

## Usage/Functionality

### Add Run

Allows users to input a shoe name and allocate distance to it for a run they have completed, which updates the shoe's mileage accordingly.

### View Shoe Mileage

Displays a list of all shoes tracked and the mileage associated with them.

### Add New Shoe

Enables users to add a new shoe to the tracker with an initial mileage of 0.

### Delete Shoe

Allows users to remove a shoe from the data which will delets the shoe and it's mileage stored with it.

## Data Persistence

Data is stored in `shoe_database.json`:
- **Loading Data**: Data is loaded from `shoe_database.json` when the program starts.
- **Saving Data**: Changes made during program execution are saved back to `shoe_database.json` before exiting.

## Error Handling

- Handles file not found errors when `shoe_database.json` is missing.
- Manages permission denied errors when the program lacks write access to `shoe_database.json`.
- Performs input validation to ensure correct data formats and prevent errors.

## Dependencies

- No external dependencies are required beyond Python standard libraries.

## Contributing

Contributions to the Shoe Mileage Tracker project are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or feedback, please contact [Your Name](mailto:your_email@example.com).

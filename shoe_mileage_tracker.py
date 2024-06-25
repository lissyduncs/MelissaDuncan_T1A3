import logging
import sys
import csv

logger = logging.getLogger()

shoe_database_filename = "data/shoe_database.csv"

def init_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)


def get_users_mode():
    print("=== Shoe Milage ===")
    print("Please choose from the following")
    print("1. Enter Milage")
    print("2. Check Milage")
    print("3. New shoe")

    #TODO: Get mode from commandline, check valid mode
    mode = 1  # For now hard-code to 1
    return mode

# [['shoe_name', 'shoe_milage'], ['test_shoe1', '0'], ['test_shoe2', '0'], ['test_shoe3', '23']]
# [{'shoe_name': 'test_shoe1', 'shoe_milage': '0'}, {'shoe_name': 'test_shoe2', 'shoe_milage': '0'}, {'shoe_name': 'test_shoe3', 'shoe_milage': '23'}]

def read_dictionary_from_csv_file(filename) -> list:
    rows = []
    print("Reading shoes from file: {}".format(filename))
    with open(filename, "r") as csvfile:  #open file for reading
        for row in csv.DictReader(csvfile):
            rows.append(row)
    print("Read {} records from file".format(len(rows)))
    print("Read records {}".format(rows))
    return rows


def find_matching_shoe_row(shoe, shoes_list):
    matching_shoe_row = None
    for row in shoes_list:
        if row["shoe_name"] == shoe:
            matching_shoe_row = row
    if matching_shoe_row is None:
        raise ValueError("Couldn't find a shoe \"{}\" in shoe list".format(shoe))
    return matching_shoe_row


def lookup_existing_milage(shoe: str) -> int:
    all_shoes_list = read_dictionary_from_csv_file(shoe_database_filename)
    shoe_record = find_matching_shoe_row(shoe, all_shoes_list)
    existing_milage_str = shoe_record["shoe_milage"]

    existing_milage = int(existing_milage_str)
    print("Lookup existing milage for shoe: {} returned: {}".format(shoe, existing_milage))
    return existing_milage


def store_shoe_milage(shoe, new_milage):
    print("Storing milage for shoe: {} = {}".format(shoe, new_milage))


def enter_and_update_milage():
    #TODO: Get shoe from user, validate is an existing shoe
    shoe = "test_shoe3"
    print("Shoe selected: {}".format(shoe))

    #TODO: Get milage from user input
    additional_milage = 10
    print("Milage entered: {}".format(additional_milage))

    #lookup old milage for shoe
    old_milage = lookup_existing_milage(shoe)

    new_milage = old_milage + additional_milage
    print("New milage for shoe: {} is {}".format(shoe, new_milage))

    store_shoe_milage(shoe, new_milage)



def check_milage():
    pass


def main():
    mode = get_users_mode()
    print("Mode selected: {}".format(mode))
    if mode == 1:
        enter_and_update_milage()
    elif mode == 2:
        check_milage()



if __name__ == '__main__':
    init_logging()
    main()


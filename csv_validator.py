"""
module to check the validity of a requested .csv file (as a in module input)
"""
import csv
import os


def csv_validator():
    """
    function to request .csv filename as input from the user, validate .csv name
    and verify that the file exists in the working directory, and is not empty nor corrupted
    :return: validated csv filename
    """

    while True:
        # input for csv filename (make sure matching .csv file is in the directory)
        csv_file_name = input("Enter filename(.csv) which contains the list of files to sort--> ")

        # make sure csv_file_name is not empty
        if not csv_file_name:
            print("filename cannot be empty")
            continue

        # check to make sure that file extension is .csv
        csv_file_ext = os.path.splitext(csv_file_name)[1]
        if csv_file_ext != '.csv':
            print(f"\nThe filename you've entered ({csv_file_name}) does not end with .csv\n"
                  "this was auto corrected for you")
            csv_file_ext = '.csv'
            csv_file_name = os.path.splitext(csv_file_name)[0] + csv_file_ext
            print(f'and now is {csv_file_name}\n')

        # check for file existence in the working directory
        csv_file_found = False
        for file in os.listdir():
            if file == csv_file_name:
                csv_file_found = True
        # if the file wasn't found, prompt again
        if not csv_file_found:
            print(f"Could not find {csv_file_name}, try again\n")
            continue

        # if the file is empty
        if os.stat(csv_file_name).st_size == 0:
            print(f"the file {csv_file_name} is empty, try a different file\n")
            continue

        try:
            # verify file not messed up using comparing to ASCII values
            with open(csv_file_name, 'r') as csv_fd:
                file_valid = True
                csv_reader = csv.reader(csv_fd)
                for line in csv_reader:
                    for item in line:
                        for letter in item:
                            if not letter.isascii():
                                file_valid = False
            if not file_valid:
                print(f"the file ({csv_file_name}) seems corrupted, try again\n")
                continue
            return csv_file_name
        except FileNotFoundError:
            print(f'error opening file ({csv_file_name}): file not found\n')
        except Exception as e:
            print(f'error opening file ({csv_file_name}): {e}\n')

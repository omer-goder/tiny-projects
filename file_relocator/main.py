import os

from csv_validator import csv_validator
from partial_name import create_files_dict, file_list, tabular_print
from file_lister import list_by_full_name, list_by_base_name
from relocation import file_relocator
# example dict returned
# {'sub_1': {'.PDF': 'V', '.SLDPRT': 'V', '.X_t': 'V'}, 'sub_2': {'.PDF': 'V', '.SLDPRT': 'V', '.X_t': ''}}
while True:
    print("Created by Omer Goder\nemail: omer.goder91@gmail.com\n")
    csv_file_name = csv_validator()

    csv_content_type = input("enter the type of content inside the csv:\n"
                             "1. full filenames (filename base+extension)\n"
                             "2. base filenames (filename base)\n"
                             "3. partial filename (some text from the filename base)\n-->")
    if csv_content_type == '1':
        complete_file_list = list_by_full_name(csv_file_name)
    elif csv_content_type == '2':
        complete_file_list = list_by_base_name(csv_file_name)
    elif csv_content_type == '3':
        files_dict = create_files_dict(csv_file_name)
        print_table_choice = input("Would you like to print all files as a table? [y/n] ")
        if print_table_choice.lower() == 'y':
            tabular_print(files_dict)
        complete_file_list = file_list(files_dict)
        # print(complete_file_list)
    else:
        input(f"{csv_content_type} is not a valid input (1, 2 or 3) only\npress Enter to continue")
        os.system('cls')
        continue

    # directory management

    while True:
        file_operation = input("select what to to with the files\n1. move\n2. copy\n-->")
        if file_operation == '1' or file_operation == 'move':
            file_operation = 'move'
            break
        elif file_operation == '2' or file_operation == 'copy':
            file_operation = 'copy'
            break
        else:
            print(f"{file_operation} is not a valid choice,")
            continue
    file_relocator(complete_file_list, operation=file_operation)

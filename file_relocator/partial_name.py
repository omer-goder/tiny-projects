"""
module to sort all filenames from the received csv file into a python dictionary,
move from dict to a list of all the full filenames / print as table
"""
import os
import csv
import shutil


def create_files_dict(csv_file_name: str):
    """
    function which receives a verified csv file name and returns a dictionary
    with all the filenames and file extension in the working directory, which
    match their name contain the value from the csv (partial name)
    :param csv_file_name: verified csv file name (str)
    :return: python dict in the following format:

    {filename1: {file_ext1: '', file_ext2: 'V'},
    filename2: {file_ext_1: 'V', file_ext_2: 'V'}}

    where file_ext value is:
    'V' - if a file with the name of filename.file_ext exists in working directory
    ''  - if a file with the name of filename.file_ext does not exists in working directory
    """

    SKUs = []  # list of SKU's in the csv file
    with open(csv_file_name, 'r') as csv_fd:
        csv_reader = csv.reader(csv_fd)
        for line in csv_reader:
            for SKU in line:
                SKUs.append(SKU)

    # creating a list of file extensions [.ext, ...]
    file_extensions = []
    for SKU in SKUs:
        for dir_file in os.listdir():
            if SKU in os.path.splitext(dir_file)[0]:
                dir_file_ext = os.path.splitext(dir_file)[1]
                if dir_file_ext not in file_extensions:
                    file_extensions.append(dir_file_ext)
    file_extensions.sort()  # sorting by ascii for constant format view
    # print("debug:::file_extensions", file_extensions)

    ext_format_dict = {}  # base format for creating extension dict (to be copied for each iteration)
    for ext in file_extensions:
        ext_format_dict[ext] = ''

    files = {}
    for filename_base in SKUs:
        for dir_file_0 in os.listdir():
            current_file_extensions = ext_format_dict.copy()  # reset dict values for each file
            if filename_base in os.path.splitext(dir_file_0)[0]:
                #  need to take the dir_file_base and re-iterate over listdir to find all exact name filenames
                for dir_file_1 in os.listdir():
                    if os.path.splitext(dir_file_0)[0] == os.path.splitext(dir_file_1)[0]:
                        dir_file_base = os.path.splitext(dir_file_1)[0]
                        dir_file_ext = os.path.splitext(dir_file_1)[1]
                        if dir_file_ext in list(current_file_extensions.keys()):
                            current_file_extensions[dir_file_ext] = 'V'
                        files[dir_file_base] = current_file_extensions

    return files


def file_list(files_dict: dict):
    """
    function to convert the files_dict created by file_lister_dict from this module
    format: {filename1: {ext1: '', ext2: 'V'}, filename2: {ext1: ...
    into a list of  full filenames (with extension) [filename1.ext1, filename2...

    :param files_dict: dict of filenames and extensions format: {filename1: {ext1: '', ext2: 'V'}, filename2: {ext1: ...
    :return: complete list of filenames with extensions [filename1.ext1, ...
    """
    files_to_transfer = []
    for file_base, ext_dict in files_dict.items():
        for file_ext in ext_dict.keys():
            if ext_dict[file_ext]:
                full_filename = file_base + file_ext
                files_to_transfer.append(full_filename)
    return files_to_transfer


def tabular_print(files_dict: dict):
    """
    function to print a table of all files and extensions as returned
    from the file_lister_dict from this module
    :param files_dict:
    :return: None
    """
    # create a list of file extensions
    file_extensions = []
    for filename in files_dict.keys():
        for file_ext in files_dict[filename].keys():
            # print("debug:::", file_ext)
            file_extensions.append(file_ext)
        break
    # go through all the files and print them in a table with the file extension as the top row
    sep_line_len = 40 + 10 * len(file_extensions)  # separator line length = max_filename_len [35] + 10*number of ext
    # print the first row
    print("filename".ljust(40), end='')
    for ext in file_extensions:
        print("|" + ext.center(9), end='')
    print()
    print(''.center(sep_line_len, '='))
    # print the rest of the files
    for filename, ext_dict in files_dict.items():
        print(filename.ljust(40), end='')
        for ext in ext_dict.keys():
            if ext_dict[ext]:
                print("|" + "V".center(9), end='')
            else:
                print("|" + " ".center(9), end='')
        print()
        print(''.center(sep_line_len, '-'))

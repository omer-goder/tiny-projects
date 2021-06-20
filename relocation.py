"""
module for creating a new directory and moving/copying files to the new directory
"""
import os
import shutil


def dir_creator(operation: str):
    """
    creating a new directory
    :param operation: operation name ('move' or 'copy') just for printing purposes
    :return dir_name: name of the created (or existed) directory
    """
    while True:
        dir_name = input(f"enter new directory name to {operation} files into: ")
        try:
            if not os.path.isdir(dir_name):  # if directory does not exist
                os.mkdir(dir_name)
                print(f"{dir_name} created successfully")
                break

            else:  # directory exists
                if os.listdir(dir_name):  # if the directory is not empty
                    print(f"\n\n!=!=!=WARNING=!=!=!\ndirectory {dir_name} is NOT empty\n"
                          "continuing to move/copy new files will erase the files with the same name "
                          "in the new directory")
                else:  # directory empty
                    print(f"the directory name {dir_name} already exists, but seems to be empty")
                dir_exists_choice = input("would you wish to continue in the same directory? [y/n] ")
                if dir_exists_choice.lower()[0] == 'y':
                    break
                else:
                    continue

        except Exception as e:
            print("error creating directory: ", e)
            break
    return dir_name


def file_relocator(files_to_move: list, operation: str):
    """
    function that take a list of full filenames (with extension), operation
    and perform the operation on all the matching files in the working directory
    the function also creates a new directory using the dir_creator function from this module
    :param files_to_move: list a full filenames (with extension)
    :param operation: str : ('move'/'copy')
    :return: None
    """
    dir_name = dir_creator(operation)

    # creating an initial list of all files in the working directory that match the file_lst
    working_dir_files_initial = []
    for dir_file in os.listdir():
        if dir_file in files_to_move:
            working_dir_files_initial.append(dir_file)

    # moving/copying all files to the new directory according to the operation
    for dir_file in os.listdir():
        if dir_file in files_to_move:
            try:
                if operation == 'move':
                    shutil.move(dir_file, os.getcwd() + f"\\{dir_name}\\{dir_file}")
                    print("file moved:", dir_file)
                elif operation == 'copy':
                    shutil.copy(dir_file, os.getcwd() + f"\\{dir_name}\\{dir_file}")
                    print("file copied:", dir_file)
                else:
                    input(f"{operation} is not a valid operation ['move' or 'copy'] only")
                    break

            except Exception as e:
                if operation == 'move':
                    print("error moving file:", dir_file, e)
                elif operation == 'copy':
                    print("error copying file:", dir_file, e)

    working_dir_files_not_moved = []  # later used for checking if all the files moved successfully
    if operation == 'move':
        for dir_file in os.listdir():
            if dir_file in working_dir_files_initial:
                working_dir_files_not_moved.append(dir_file)

    new_dir_files = []  # creating a list of all files in the new directory
    for dir_file in os.listdir(dir_name):
        new_dir_files.append(dir_file)

    files_not_copied = []  # later used for checking if all the files copied successfully
    if operation == 'copy':
        for initial_file in working_dir_files_initial:
            if initial_file not in new_dir_files:
                files_not_copied.append(initial_file)

    # checks and output for user using input statements
    while True:
        if operation == 'move':
            if len(new_dir_files) == len(working_dir_files_initial) and not working_dir_files_not_moved:
                input("\n\nOperation finished successfully\npress Enter to continue...")
                break
            elif len(new_dir_files) < len(working_dir_files_initial):
                input("\n\nIt seems that not all files were moved\n"
                      "press Enter to see the list of files that did not move\n")
                for file in working_dir_files_not_moved:
                    print(file)
                input("\npress Enter to continue\n")
                break
            elif len(new_dir_files) == 0:
                input("\n\nIt seems that no files were moved\n"
                      "try again, making sure all inputs are correct\n")
                break
            else:  # in case of some unknown case
                input("\n\nIt seems that there was an issue with transferring some of the files\n"
                      "it is suggested to run the program again on the same csv file, "
                      "or make sure that everything is ok\n"
                      "press Enter to continue\n")
                break

        elif operation == 'copy':
            if len(new_dir_files) == len(working_dir_files_initial):
                input("\n\nOperation finished successfully\npress Enter to continue...")
                break
            elif len(new_dir_files) < len(working_dir_files_initial):
                input("\n\nIt seems that not all files were copied\n"
                      "press Enter to see the list of files that did not copy\n")
                for file in files_not_copied:
                    print(file)
                input("press Enter to continue\n")
                break
            elif len(new_dir_files) == 0:
                input("\n\nIt seems that no files were copied\n"
                      "try again, making sure all inputs are correct\n")
                break
            else:  # in case of some unknown case
                input("\n\nIt seems that there was an issue with transferring some of the files\n"
                      "it is suggested to run the program again on the same csv file, "
                      "or make sure that everything is ok\n"
                      "press Enter to continue\n")
                break
    os.system('cls')

"""
module to create a simple list of filenames from a csv data
according to the requirement (full name [with extension] / base name [no extension])
"""
import os
import csv


def list_by_full_name(csv_file_name: str):
    """
    function to accept csv file with full filenames
    and return a list of files to move (exists both on the csv and in the working directory)
    :param csv_file_name:
    :return:files_to_move (list of files that exists both on the csv and in the working directory)
    """
    full_names = []
    with open(csv_file_name, 'r') as csv_fd:
        csv_reader = csv.reader(csv_fd)
        for line in csv_reader:
            for full_name in line:
                full_names.append(full_name)

    files_to_move = []
    for dir_file in os.listdir():
        if dir_file in full_names:
            files_to_move.append(dir_file)

    return files_to_move


def list_by_base_name(csv_file_name: str):
    """
    function to accept csv file with base filenames (no extension)
    and return a list of files to move (exists both on the csv [with no extension] and in the working directory)
    :param csv_file_name:
    :return:files_to_move (list of files that exists both on the csv and in the working directory)
    """
    base_names = []
    with open(csv_file_name, 'r') as csv_fd:
        csv_reader = csv.reader(csv_fd)
        for line in csv_reader:
            for base_name in line:
                base_names.append(base_name)

    files_to_move = []
    for dir_file in os.listdir():
        if os.path.splitext(dir_file)[0] in base_names:
            files_to_move.append(dir_file)

    return files_to_move

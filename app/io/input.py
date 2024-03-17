import pandas as pd


def input_from_console():
    """
    Function to get text from user through console
    :return:
        (str): input text
    """
    text = input("Enter some text: ")
    return text


def read_from_file_original(path_to_file):
    """
    Function to read data from file with builtin functional
    :param
        path_to_file (str): path to the file to read data from
    :return:
        str: data from file
    """
    with open(path_to_file, 'r') as f:
        data = f.read()
    return data


def read_from_file_pandas(path_to_file):
    """
    Function to read data from csv file with pandas functional
    :param
        path_to_file (str): path to the file to read data from
    :return:
        data from file
    """
    data = pd.read_csv(path_to_file)
    return data

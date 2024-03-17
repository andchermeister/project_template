import pandas as pd


def input_from_console():
    text = input("Enter some text: ")
    return text


def read_from_file_original(path_to_file):
    with open(path_to_file, 'r') as f:
        data = f.read()
    return data


def read_from_file_pandas(path_to_file):
    data = pd.read_csv(path_to_file)
    return data

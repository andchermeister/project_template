def output_to_console(text):
    """
    Function to output text written in console
    :param
        text (str): text to output
    """
    print(text)


def write_to_file_original(path_to_file, data):
    """
    Function to write data to file with builtin functional
    :param
        path_to_file (str): path to the file to write data to
    :param
        data (str): data to write to file
    """
    with open(path_to_file, 'w') as f:
        f.write(data)

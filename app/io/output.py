def output_to_console(text):
    print(text)


def write_to_file_original(path_to_file, data):
    with open(path_to_file, 'w') as f:
        f.write(data)

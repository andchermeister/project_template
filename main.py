from app.io.input import input_from_console, read_from_file_original, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_original


def main():
    # Console input
    input_text = input_from_console()
    output_to_console(input_text)
    write_to_file_original('data/console_output_1.txt', input_text)

    # File input
    file_text = read_from_file_original('data/file_to_input.txt')
    output_to_console(file_text)
    write_to_file_original('data/console_output_2.txt', file_text)

    # File input with pandas
    file_pandas = read_from_file_pandas('data/file_for_pandas.csv')
    output_to_console(file_pandas)


if __name__ == "__main__":
    main()

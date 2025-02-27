def read_file_line_by_line(abc):
    try:
        with open(abc, 'r') as file:
            for line in file:
                print(line, end='')  # The `end=''` avoids adding extra newline
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_file_line_by_line("ABC.txt")

#output
hello everyone


def count_words_in_file(abc):
    word_count = 0
    try:
        with open(abc, 'r') as file:
            for line in file:
                # Split the line into words based on whitespace and count them
                words = line.split()
                word_count += len(words)
        print(f"Total number of words in the file '{abc}': {word_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
count_words_in_file("ABC.txt")

#output
Total number of words in the file 'ABC.txt': 2




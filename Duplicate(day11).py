def remove_duplicates(input_str):
    words = input_str.split()
    result = []
    
    for word in words:
        # Convert to set to remove duplicates and join back to string
        unique_word = ''.join(sorted(set(word), key=word.index))
        result.append(unique_word)

    print(" ".join(result))

# Input
input_str = "String and String Function"
remove_duplicates(input_str)


#o/p

String and String Functio

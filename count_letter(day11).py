def count_characters(input_str):
    chars = 0
    digits = 0
    symbols = 0

    for char in input_str:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    print(f"Chars = {chars}")
    print(f"Digits = {digits}")
    print(f"Symbols = {symbols}")

# Input
input_str = "P@#yn26at^&i5ve"
count_characters(input_str)

#o/p
Chars = 8
Digits = 3
Symbols = 4

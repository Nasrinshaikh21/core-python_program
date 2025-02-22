# define Function
def find_duplicates(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates

# Example usage:
numbers = [1, 2, 3, 4, 5, 2, 3, 6]
print("Duplicate values:", find_duplicates(numbers))

#output
Duplicate values: [2, 3]

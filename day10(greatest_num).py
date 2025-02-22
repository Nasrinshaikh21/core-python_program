#define Function
def find_largest_and_smallest(lst):
    if len(lst) == 0:
        return None, None

    largest = lst[0]
    smallest = lst[0]

    for number in lst:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage:
numbers = [10, 20, 4, 45, 99]
largest, smallest = find_largest_and_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)


#output

Largest number: 99
Smallest number: 4


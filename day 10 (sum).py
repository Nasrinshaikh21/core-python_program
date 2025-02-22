#defining list Function
def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
     return total

numbers = [1,2,3,4,5]
print("sum of list is :" , sum_of_list(numbers))
    

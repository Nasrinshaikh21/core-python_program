# Finding square of a Number

#Function declaration
def square(a):
    if a**2:
        return a**2
    else:
        return"no square found"
a=int(input("enter a number"))
result = square(a)
print(f"the square is : {result}")

#o/p

enter a number10
the square is : 100

enter a number0
the square is : no square found

        

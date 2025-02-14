#divison of two numbers

# Function Declaration
def div(a,b):
    if b!=0:
        return a/b
    else:
        return"cannot divide by zero"
# Variable Declaration
a=int(input("enter number"))
b=int(input("enter number"))
#Function call
result = div(a,b)
print(f"the result is:{result}")

#O/P:
enter number30
enter number10
the result is:3.0


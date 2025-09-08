# We Define the Function Named "factorial"
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)


# We then take the input from the User
n = int(input("Enter the number you want FACTORIAL: "))

# Call the factorial function
fact = factorial(n)
print('The Factorial of ', n, 'is', fact)

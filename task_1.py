# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

# def factorial(n):
#     if n<2:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

fact=1
def factorial(n):
    global fact
    if n==0:
        return 1
    
    for i in range(1,n+1):
        fact = fact*i
    return fact

num = int(input("Enter a number:"))
print(f'Factorial of {num} is:', factorial(num))
'''
assignment 3 task 1
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and
     calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
a=int(input("Enter a number: "))
print(f"factorial of {a} is {factorial(a)}")


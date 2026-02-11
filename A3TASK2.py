'''Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''

import math
a=int(input("Enter a number: "))
sq_root=math.sqrt(a)
log=math.log(a)
si=math.sin(a)
print(f"Square root:{sq_root}")
print(f"Logarithm: {log}")
print(f"Sine: {si}")
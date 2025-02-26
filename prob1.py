# Write a user-defined function named add_numbers(num1, num2) that takes two numbers as arguments and returns their sum.
# Use a print statement to display the result in a clear format.

#user defined function with 2 parameters
def add_numbers(num1, num2):
        return num1 + num2

#variables to store the value of two operands
x = 203
y = 34

sum = add_numbers(x, y) #call the add_numbers function to get the sum of x & y then store it to variable

print(x, " + ", y, " = ", sum) #display the result with clear format
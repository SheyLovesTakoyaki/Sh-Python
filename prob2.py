# Write a user-defined function named string_length(input_string) that takes a string as an argument and returns its length using the built-in len() function.
# Use a print statement to display the result in a clear format.

#user defined function with string parameter
def string_length(input_string):
    return print("Length of a string: ", len(input_string)) #prints the user input with format

 #accepts the input then passing it to string_length
string_length(input("Enter a string: "))
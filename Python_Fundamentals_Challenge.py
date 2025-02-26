# #File Handling - Create a program that writes a list of names to a text file and then reads the file to display the names.

# #this block of code creates and write the file using append (a)
# f = open("Names.txt", "a")
# f.write("Hershey\n" "Angela\n" "AJ\n" "Hermo\n")
# f.close()

# #this reads the file Names.txt
# f = open("Names.txt", "r")
# print(f.read())

#Write a program that creates a list of numbers and prints the sum and average of the numbers.
# numbers = [1, 2, 3, 5, 4, 100, 89]
# sum_of_numbers = sum(numbers)
# average = sum_of_numbers / len(numbers)
# formatted_average = "%.2f"%average

# print("Sum: ", sum_of_numbers)
# print("Average: ", formatted_average)

#Create a program that defines a tuple with at least five elements and prints the second and fourth elements.
# favorite_foods = ("bananaque", "cheesecake", "chocolate", "Skyflakes dipped in condensed milk", "oreo ice cream")
# print(favorite_foods[1], favorite_foods[-2])

#Write a program that creates two sets and performs union, intersection, and difference operations, printing the results.
# set_1 = {"iphone", "samsung", "xiaomi"}
# set_2 = {"tecno", "oppo", "xiaomi"}

# union_set = set_1 | set_2
# intersection_set = set_1 & set_2
# difference_set = set_1 - set_2

# print(union_set)
# print(intersection_set)
# print(difference_set)

#Create a program that defines a dictionary with at least three key-value pairs and prints each key with its corresponding value.
his_dict = {
    "Program": "Computer Science",
    "Expertise": "AI",
    "Year": "3rd Year"
}

for key, value in his_dict.items():
    print(f"{key}: {value}")
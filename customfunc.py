# # custom function to create a value
# def average(values):
#     # calculate the results
#     average_value = sum(values) / len(values)

#     # round the results
#     rounded_average = round(average_value, 2)

#     # return the the rounded results
#     return rounded_average # OR return round(average_value, 2)

# sales = [125.92, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# # calculating the average
# print(average(sales)

# def clean_string(text):
#     # replace spaces with underscores
#     no_spaces = text.replace(" ", "_")

#     #convert to lowercase
#     clean_text = no_spaces.lower()

#     return clean_text

# print(clean_string("i loVE dAtACAmp!"))

# x = 20

# print(id(x))

# def change(one, *two):

#     print(type(two))

#     change(1,2,3,4)


# def greet_people(people: list[str]) -> None:
#     for person in people:
#         print(f"Hello, {person.capitalize()}!")

# greet_people(["Hershey", "Angela"])

class Fruit:
    ...

fruit: Fruit = Fruit()
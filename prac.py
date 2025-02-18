# first_num = int(input('1: '))
# operation = input('operation +, -, *, /: ')
# second_num =int(input('2: '))

# if operation == '+':
#     print('Result: ', first_num + second_num)
# elif operation == '-':
#     print('Result: ', first_num - second_num)

weight = float(input('Weight: ' ).lower())
unit = input("(K)g or (L)bs: ")

if unit == 'k': 
    print('Weight in Kg: ', weight /  0.45)
elif unit == 'l':
    print('Weight in pounds: ', weight * 0.45)
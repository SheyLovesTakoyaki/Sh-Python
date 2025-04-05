# class Microwave:
#     def __init__(self, brand: str, power_rating: str) -> None:
#         self.brand = brand
#         self.power_rating = power_rating
#         self.turned_on: bool = False

# # method
#     def turn_on(self) -> None:
#         if self.turned_on:
#             print(f'Microwave ({self.brand}) is already turned on.')
#         else:
#             self.turned_on = True
#             print(f'Microwave ({self.brand}) is now turned on.')

#     def turn_off(self) -> None:
#         if self.turned_on:
#             self.turned_on = False
#             print(f'Microwave ({self.brand}) is now turned off.')
#         else:
#             print(f'Microwave ({self.brand}) is already turned off.')

#     def run(self, seconds: int, ) -> None:
#         if self.turned_on:
#             print(f'Running ({self.brand}) for {seconds} seconds')
#         else:
#             print(f'A mystical force whispers: "Turn on your microwave first..."')

#     # Dunder Method
#     def __add__(self, other):
#         return f'{self.brand} + {other.brand }'
    
#     def __mul__(self, other):
#         return f'{self.brand} * {other.brand }'
    
#     def __str__(self) -> str:
#         return f'{self.brand} (Rating: {self.power_rating})'


# smeg: Microwave = Microwave('Smeg', 'B')
# bosch: Microwave = Microwave('Bosch', 'C')

# print(smeg + bosch)
# print(smeg * bosch)
# print(smeg)
# print(bosch)
# # smeg.turn_on()
# # smeg.run(30)
# # smeg.turn_off()
# # smeg.run(20)

# # print(smeg)
# # print(smeg.brand)
# # print(smeg.power_rating)

# # bosch: Microwave = Microwave('Bosch', 'C')
# # print(bosch.brand)
# # print(bosch.power_rating)

# class test:
#     def __init__(self, a):
#         self.a = a

#     def display(self):
#         print(self.a)

# obj = test()
# obj.display()

# class Sales:   

#     def __init__(self, id):       

#         self.id = id       

#         id = 100

# val = Sales(129)

# class change:
#     def __init__(self, x, y, z):
#         self.a = x+y+z

# x = change(1,2,3)
# y = getattr(x, 'a')
# setattr(x, 'a', y+1)
# print(x.a)

# class A():
#     def disp(self):
#         print("A disp()")

# class B(A):
#     pass

# obj = B()
# obj.disp()

class fruits:
    def __init__(self, price):
        self.price = price
obj = fruits(50)

obj.quantity=10
obj.bags=2

print(obj.quantity+len(obj.__dict__))
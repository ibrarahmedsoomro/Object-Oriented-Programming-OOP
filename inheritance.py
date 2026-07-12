# Inheritance with Super Method
class Mobiles:
    def __init__(self, name):
        self.name = name

class Xiaomi(Mobiles):
    def __init__(self, name, functionality):
        super().__init__(name)
        self.functionality = functionality

laptop = Xiaomi("Redmi", "Turbo")
print(laptop.name)
print(laptop.functionality)
# class ProProgrammer(Programmer):
#      pass

# Bignner = Programmer("Ibrar")
# print(Bignner.name)






                # Inheritance

# class Programmer:
#     def __init__(self, name):
#          self.name = name

# class ProProgrammer(Programmer):
#      pass

# Bignner = Programmer("Ibrar")
# print(Bignner.name)

# class Suzuki:
#     def mehran(self):
#         print("Hello mehran")

# class KIA:
#     pass
# cars = Suzuki()
# cars.mehran()

# # class Person:
# #     def speak(self):
# #         print("Person is Speaking Parrent  Class")
    
# # class Student:
# #     def shagrid(Person):
# #         print("Child Class")

# # student1 = Student()
# # student1.speak()
class Device:
    def __init__(self, comapny, warranty):
        self.company = comapny
        self.warranty = warranty

class Laptop(Device):
    def __init__(self, comapny, warranty, processor):
        super().__init__(comapny, warranty)
        self.processor = processor
    
device1 = Laptop("NOKIA", "12 Months", "G99")

print(device1.company)
print(device1.warranty)
print(device1.processor)


# class Employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary = salary

# class EmployeeData(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

# emp1 = EmployeeData("Ibrar", 30000, "IT")

# print(emp1.name)
# print(emp1.salary)
# print(emp1.department)



# class Laptops:
#     def __init__(self, name):
#         self.name = name

# class Dell(Laptops):
#     def __init__(self, name, specs):
#         super().__init__(name)
#         self.specs = specs

# std = Dell("Dell", "Core i5 3rd  Generation")
# print(std.name)
# print(std.specs)


# # Inheritance with Super Method
# class Mobiles:
#     def __init__(self, name):
#         self.name = name

# class Xiaomi(Mobiles):
#     def __init__(self, name, functionality):
#         super().__init__(name)
#         self.functionality = functionality

# laptop = Xiaomi("Redmi", "Turbo")
# print(laptop.name)
# print(laptop.functionality)
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
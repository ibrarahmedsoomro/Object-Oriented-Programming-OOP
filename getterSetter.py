class CommercialBank:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, newName):
        self.__name = newName
bankName = CommercialBank("UBL")
bankName.set_name("ABL")
print(bankName.get_name())


# class Student:
#     def __init__(self, name):
#         self.__name = name
    
#     def get_name(self):
#         return  self.__name
    
#     def set_name(self, new_name):
#         if new_name !=  "":
#             self.__name = new_name
#         else:
#             print("Invalid Name")

# student = Student("Ibrar Ahmed")
# student.set_name("Ahmed")

# print(student.get_name())
# class Student:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name
# student = Student("Ali")
# print(student.get_name())
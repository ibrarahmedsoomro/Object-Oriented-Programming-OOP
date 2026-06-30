class Student:
    def __init__(self, name , age):
        self.name = name
        # self.name= name
        self.age = age
        # self.age = age


student1 = Student("Ali",20)
student2 = Student("Ibrar",30)


student1.name = "Ahmed"
student2.name = "Soomro"



print(student1.name, )
print(student2.name)

# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
# student1 = Student("Ibrar Ahmed", 30)

# print(student1.name)
# print(student1.age)

# class Student:
#     def __init__(self):
#         self.name = "Ibrar Ahmed"
#         self.age = 30

# student1 = Student()
# student2 = Student()

# print(student1.name)
# print(student2.age)
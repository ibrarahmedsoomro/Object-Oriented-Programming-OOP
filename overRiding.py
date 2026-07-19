class Parent:
    def work(self):
        print("Parent Work")

class Son(Parent):
    def work(self):
        super().work()
        print("Son Work")

s = Son()
s.work()

# class Parent:
#     def work(self):
#         print("This is a Parent Class")

# class Son(Parent):
#     def work(self):
#         print("This is Son Class")


# parent = Son()
# parent.work()
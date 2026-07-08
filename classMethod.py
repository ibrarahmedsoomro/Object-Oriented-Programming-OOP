class Laptop:
    laptop_name = "DELL"
    @classmethod
    def change_laptop_name(cls, name):
        cls.laptop_name  = name
Laptop.change_laptop_name("Lenovo")
print(Laptop.laptop_name)

# class School:
#     school_name = "GBPS URDU"
#     @classmethod

#     def change_name(cls, name):
#         cls.school_name = name

# School.change_name("GBPS Majeedia")

# print(School.school_name)

# class Bank:
#     bank__name = "UBL"
#     @classmethod
#     def change_bank(cls,name):
#         cls.bank__name = name

# Bank.change_bank("NBP")

# print(Bank.bank__name)


# class StaticVar:
#     @staticmethod
#     def add(a, b):
#         return a * b

# print(StaticVar.add(20,30))

# class Bank:

#     bank_name = "HBL"

#     @classmethod
#     def change_bank(cls, name):
#         cls.bank_name = name

# Bank.change_bank("UBL")

# print(Bank.bank_name)


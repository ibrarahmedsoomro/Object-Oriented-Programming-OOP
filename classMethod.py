class Bank:
    bank__name = "UBL"
    @classmethod
    def change_bank(cls,name):
        cls.bank__name = name

Bank.change_bank("NBP")

print(Bank.bank__name)


# class Bank:

#     bank_name = "HBL"

#     @classmethod
#     def change_bank(cls, name):
#         cls.bank_name = name

# Bank.change_bank("UBL")

# print(Bank.bank_name)
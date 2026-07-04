class Microsoft:
    def __init__(self, company, employee, salary):
        self._company = company
        self._employee = employee
        self._salary = salary

company1 = Microsoft("Microsoft", "Ibrar Ahmed", 750000)
company2 = Microsoft("Tesla", "Ahmed", 800000)
company3 = Microsoft("BYD", "Ali", 750000)

print(company1._company)
print(company2._employee)
print(company3._salary)
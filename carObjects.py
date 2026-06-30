class Car:
    def __init__(self, company, model, color, price):
        self.company = company
        self.model = model
        self.color = color
        self.price = price

car1 = Car("Toyota", 2018, "White", 500000000)
car2 = Car("Colorla", 2015, "Black", 2000000)

print(car1.company, car1.model, car1.color, car1.price)
print(car2.company, car2.model, car2.color, car2.price)
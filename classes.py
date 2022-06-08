class vehicle:
    name = ""
    kind = "car"
    color = ""
    price = 100.00

    def description(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth ${self.price}"
        return desc_str

car1 = vehicle()
car2 = vehicle()

car1.name = "Mercedes"
car1.color = "red"
car1.price = 60000

car2.name = "BMW"
car2.color = "blue"
car2.price = 20000

print(car1.description())
print(car2.description())
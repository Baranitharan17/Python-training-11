class car:
    def __init__(self, brand, name, year):
        self.brand= brand
        self.name= name
        self.year= year

car1=car("Suzuki", "Baleno", 2026)
car2=car("Hyundai", "Venue", 2026)

print("Car1: ")
print("Brand :", car1.brand)
print("Name :", car1.name)
print("Year :", car1.year)

print("Car2: ")
print("Brand :", car2.brand)
print("Name :", car2.name)
print("Year :", car2.year)
        
class car:
    def __init__(self, brand, price, color):
        print("It is a car class")
        self.brand = brand
        self.price = price
        self.color = color
        print(f"brand = {self.brand}\t price = {self.price}\t color = {self.color}")

class defender(car):
    def __init__(self, brand, price, color):
        super().__init__(brand, price, color)

    def start(self):
        print("Defender Started...")

class bmw(car):
    def __init__(self, brand, price, color):
        super().__init__(brand, price, color)

    def wheel(self):
        print("BMW Wheels Rotating...")


print("enter details for DEFENDER car:")
d_brand = input("enter brand: ")
d_price = input("enter price: ")
d_color = input("enter color: ")

c = defender(d_brand, d_price, d_color)
c.start()

print("enter details for BMW car:")
b_brand = input("enter brand: ")
b_price = input("enter price: ")
b_color = input("enter color: ")

b = bmw(b_brand, b_price, b_color)
b.wheel()










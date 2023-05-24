class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        if self.quantity <= 0:
            self.active = False
            return self.active
        else:
            return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            return "ERROR AMOUNT ENTERED IS GREATER THAN THE AMOUNT OF PRODUCT"
        total = 0
        for amount in range(quantity):
            total += self.price
        total = float(total)
        self.quantity = self.quantity - quantity
        return f"The total order is ${total}", total
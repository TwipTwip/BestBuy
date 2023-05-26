class Product:
    def __init__(self, name, price, quantity):
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as error:
            return error

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
        return self.quantity

    def is_active(self):
        if self.quantity <= 0:
            self.active = False
            return self.active
        else:
            return self.active

    def activate(self):
        self.active = True
        return self.active

    def deactivate(self):
        self.active = False
        return self.active

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        assert quantity <= self.quantity, "ERROR AMOUNT ENTERED IS GREATER THAN THE AMOUNT OF PRODUCT"
        total = 0
        for amount in range(quantity):
            total += self.price
        total = float(total)
        self.quantity = self.quantity - quantity
        return f"The total order is ${total}", total


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(self, name, price)
        self.name = name
        self.price = price

    def buy(self, quantity):
        total = 0
        for amount in range(quantity):
            total += self.price
        total = float(total)
        return f"The order total is {total}", total

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(self, name, price)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.maximum = maximum
        self.total = 0

    def buy(self, quantity):
        if quantity > self.maximum or self.total >= self.maximum:
            raise Exception("Sorry, item limited to one per order")
        else:
            self.total += 1
            total = self.price
            self.quantity = self.quantity - 1
            total = float(total)
            return f"The order total is {total}", total

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
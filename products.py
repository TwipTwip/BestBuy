import promotions


class Product:
    def __init__(self, name, price, quantity):
        promotion = None
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
            self.promotion = promotion
        except Exception as error:
            return error

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def name_of_promotion(self):
        str_name = self.promotion.name_of_promotion
        return str_name

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
        if self.promotion is not None:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion}"

    def buy(self, quantity):
        assert quantity <= self.quantity, "ERROR AMOUNT ENTERED IS GREATER THAN THE AMOUNT OF PRODUCT"
        total = 0
        if self.promotion is not None:
            total = self.promotion.apply_promotion(self.price, quantity)
            self.quantity = self.quantity - quantity
            return f"The total order is ${total}", total
        else:
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
        self.promotion = None
        self.quantity = 0

    def is_active(self):
        self.active = True
        return self.active

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity):
        total = 0
        if self.promotion is not None:
            total = self.promotion.apply_promotion(self.price, quantity)
            return f"The total order is ${total}", total
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

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Sorry, item limited to one per order")
        else:
            total = self.price
            self.quantity = self.quantity - 1
            total = float(total)
            return f"The order total is {total}", total

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"

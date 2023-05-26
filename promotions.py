class Promotion:
    def __init__(self, name_of_promotion):
        self.name_of_promotion = name_of_promotion

    def apply_promotion(self, price):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name_of_promotion):
        super().__init__(self)
        self.name_of_promotion = name_of_promotion

    def apply_promotion(self, price, quantity):
        num_pairs = quantity // 2
        discounted_price = price * 0.5
        total_price = (price * num_pairs) + (discounted_price * (quantity - num_pairs))
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, name_of_promotion, percent):
        super().__init__(self)
        self.name_of_promotion = name_of_promotion
        self.percent_amount = percent

    def apply_promotion(self, price, quantity):
        return price * (quantity - self.percent_amount / 100)


class ThirdOneFree(Promotion):
    def __init__(self, name_of_promotion):
        super().__init__(self)
        self.name_of_promotion = name_of_promotion

    def apply_promotion(self, price, quantity):
        discounted_price = 0
        subtract_discount = 0
        if quantity >= 3:
            num_free_items = quantity // 3
            for times in range(num_free_items):
                subtract_discount += price
            for items in range(quantity):
                discounted_price += price
            discounted_price = discounted_price - subtract_discount
            return discounted_price
        else:
            total = 0
            for item in range(quantity):
                total += price
            return total
import products


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)
        print("Product Added")

    def remove_product(self, product):
        del (product)
        total_quantity = total_quantity - product.quantity

    def get_total_quantity(self):
        total_quantity = 0
        for items in self.products:
            total_quantity += items.quantity
        return total_quantity

    def get_all_products(self):
        list_of_active_products = []
        counter = 0
        list_of_items = []
        for product in self.products:
            if product.is_active() is False:
                del product
                counter = 0
            else:
                counter += 1
                if product.is_active() is True:
                    if product.promotion is not None:
                        if product.quantity == 0:
                            list_of_items.append(f"{counter}. {product.name}, Price: ${product.price} Quantity: Unlimited, Promotion: {product.name_of_promotion()}")
                            list_of_active_products.append(product)
                        else:
                            list_of_items.append(f"{counter}. {product.name}, Price: ${product.price} Quantity: {product.quantity}, Promotion: {product.name_of_promotion()}")
                            list_of_active_products.append(product)
                    else:
                        if product.quantity == product.price:
                            list_of_items.append(f"{counter}. {product.name}, Price: ${product.price} Quantity: Unlimited")
                            list_of_active_products.append(product)
                        else:
                            list_of_items.append(
                                f"{counter}. {product.name}, Price: ${product.price} Quantity: {product.quantity}")
                            list_of_active_products.append(product)
        return list_of_active_products, list_of_items

    def order(self, shopping_list):
        total_price = 0
        try:
            for item in shopping_list:
                if item[0] in self.products:
                    purchase = item[0].buy(item[1])
                    total_price += purchase[1]
        except TypeError:
            return purchase
        return f"Order made, the total price is ${total_price}"
import store
import products


def start(best_buy):
    while True:
        print("""
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit 
""")
        selection = input("Enter your selection: ")
        if selection == '1':
            items = best_buy.get_all_products()[1]
            print("-----")
            for item in items:
                print(item)
            print("-----")
        if selection == '2':
            print("-----")
            print(f"Total Quantity: {best_buy.get_total_quantity()}")
            print("-----")
        if selection == '3':
            print(shopping_list(best_buy))
        if selection == '4':
            print("Bye!")
            break


def shopping_list(best_buy):
    """This giant funciton makes sure that the user enters a quantity
  that can be purchased and calculate the total cost"""
    shopping_list = []
    keep_going = True
    item_choices = best_buy.get_all_products()[1]
    print("------")
    for item in item_choices:
        print(item)
    print("------")
    while keep_going:
        item_name = ""
        item_to_buy = ()
        options = best_buy.get_all_products()[0]
        product_choice = input("Enter the number of the item that you would like to buy: ")
        if product_choice == "":
            pass
        else:
            product_choice = int(product_choice)
        quantity_to_buy = input("Enter the amount you would like to buy: ")
        print("-----")
        if quantity_to_buy == "":
            keep_going = False
            return best_buy.order(shopping_list)
        else:
            quantity_to_buy = int(quantity_to_buy)
            shopping_item = options[product_choice - 1]
            item_name = shopping_item
            item_to_buy = (item_name, quantity_to_buy)
            shopping_list.append(item_to_buy)


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

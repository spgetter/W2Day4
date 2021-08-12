
class Shopping_cart:

    def __init__(self, groceries, cart_total, sub_total, cart):
        print("\n")
        response = input("Would you like to 'show'/'add'/'delete' or 'quit'?:")
        return response, cart, cart_total, sub_total

    def add_items(self):
        for key,value in groceries.items():
            print(f"{key} : ${value}")
        choice = input("Select from these items:")
        try:
            sub_total = groceries[choice]
            # cart_total += sub_total
            cart.append([choice, sub_total])
            # cart[len(cart)-1][1] = [[cart_total]]
        except: 
            print("Please only select an item in the list, typed EXACTLY as it appears")   

    def delete_items(self):
        for i in cart:
            print(f"{i[0]} : ${i[1]}")
        choice = input("Select from these items:")
        try:
            sub_total = groceries[choice]
            # cart_total -= sub_total
            cart.remove([choice, sub_total])
            # cart[len(cart)-1][1] = [[cart_total]]
        except: 
            print("Please only select an item in the list, typed EXACTLY as it appears")

    def show_cart(self):
        for i in cart:
            print(f"{i[0]} : ${i[1]}")

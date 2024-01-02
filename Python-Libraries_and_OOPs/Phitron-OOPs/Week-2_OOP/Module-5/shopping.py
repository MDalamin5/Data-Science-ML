class Shopping:
    def __init__(self, full_name) -> None:
        self.name = full_name
        self.cart = []

    
    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)

    def checkOut(self, amount):
        sum = 0
        for product in self.cart:
            sum += product['price'] * product['quantity']
        if sum <= amount:
            print(f"Check out sussfully and left amount is: {amount - sum}")
        else:
            print(f"Total bill is: {sum}, And {amount} taka is not sufficient taka. add {abs(sum - amount)} taka more")

    def remove_item(self, p_name):
        for product in self.cart:
            if product['item'] == p_name:
                self.cart.remove(product)
    

alamin = Shopping('Md Al Amin')
alamin.add_to_cart('Alu', 20, 2)
alamin.add_to_cart('Jal', 40, 1)
alamin.add_to_cart('Tomato', 80, 2)
alamin.add_to_cart('Bagun', 50, 3)
alamin.add_to_cart('Dim', 12, 15)
# print(alamin.cart)
alamin.remove_item('Alu')
print(f"           {alamin.name} Product info\n")
for product in alamin.cart:
    print(f"""Product name: {product['item']},  Price: {product['price']},  Quantity: {product['quantity']}""")

# alamin.checkOut(110000)
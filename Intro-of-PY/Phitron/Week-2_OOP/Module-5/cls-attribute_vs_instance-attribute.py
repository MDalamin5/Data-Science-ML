class Shop:
    # cart = [] # class attribute
    shopping_mall = 'Jamuna'
    def __init__(self, buyer) -> None:
        self.buyer = buyer
        self.cart = [] # is a instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)
        

mehazabeen = Shop('Meh-Jabeen')
mehazabeen.add_to_cart('alu')
print(mehazabeen.cart)

nisho = Shop('Nisho Khan')
nisho.add_to_cart('bagun')
print('Nisho buying items', nisho.cart)

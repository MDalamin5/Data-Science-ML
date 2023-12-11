class Shopping:
    cart = [] # class attribute # static attribute
    orgin = 'China'

    def __init__(self) -> None:
        self.name = 'Jamouna'
        self.location = 'Bashundhara'

    
    def purchase(self, amount, price, item):
        remaining = amount - price
        price(f'produc: {item} and remaing amount: {remaining}')


    @classmethod
    def acHauaKhauaPublic(self, namee):
        print(f"Go {self.orgin} And {namee} is a Haua khaua public not buy anythigs")

    @staticmethod
    def doProduct(a, b):
        print(a * b)


fokira_pub = Shopping()

Shopping.acHauaKhauaPublic('Al Amin')
Shopping.doProduct(2, 3)
        

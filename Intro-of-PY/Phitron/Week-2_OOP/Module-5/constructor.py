class Phone:
    manufactured = 'USA'

    def __init__(self, owner, brand, price) -> None:
        self.owner = owner
        self.brand = brand
        self.price = price

    
    def display(self):
        print(f"""
            ***The Informantion of the {self.owner} phone***
                        Wonner : {self.owner}
                        Brand  : {self.brand}
                        Price  : {self.price}
            """)
        

my_phone = Phone('Md Al Amin', 'Apple', 1200)
my_phone2 = Phone('Lowra Lacchan', 'Apple', 1500)
my_phone.display()
my_phone2.display()
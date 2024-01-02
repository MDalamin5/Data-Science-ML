class Labptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Currently running {self.brand} Laptop'
    

    def coding(self):
        return f"this laptop is best for Python coding"
    

class Phone:
    def __init__(self, brand, price, color, is_duelSIM, ram) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.is_duelSIM = is_duelSIM
        self.ram = ram

    def run(self):
        return f'Currently running {self.brand} Phone'
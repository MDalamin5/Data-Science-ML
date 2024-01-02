# Intro of inharitance

class Device:
    def __init__(self, brand, price, color, orgin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.orgin = orgin

    def run(self):
        return f"this deivice is {self.brand} Brand"
    
    def __repr__(self) -> str:
        return f"Brand: {self.brand}, Orgin: {self.orgin}"
    


class Phone(Device):
    def __init__(self, brand, price, color, orgin, ram, is_dule_sim) -> None:
        super().__init__(brand, price, color, orgin)
        self.ram = ram
        self.is_dule_sim = is_dule_sim


    def display(self):
        return f"Brand: {self.brand}, Orgin: {self.orgin}"



class Laptop(Device):
    def __init__(self, brand, price, color, orgin, ssd, os_system) -> None:
        super().__init__(brand, price, color, orgin)
        self.ssd = ssd
        self.os_system = os_system



iPhone = Phone('Apple', 12000, 'Silver', 'USA', '8GB', False)
print(iPhone)
print(iPhone.run())

class Bank:
    def __init__(self,name, address, initial_deposite) -> None:
        self.name = name
        self.__address = address
        self.__balance = initial_deposite


    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        self.__address = value


    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            return f"salary can-not be negative"
        self.__balance += value



dbbl = Bank('Md Al Amin', 'Bashundhara', 1500)

print(dbbl.balance)
dbbl.balance = 1500
print(dbbl.balance)
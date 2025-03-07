class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name # publinc
        self.__balance = initial_deposite # privet
        self._brance = 'Bashundhara' # protected

    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, amount):
        self.__balance += amount
    


user_1 = Bank('Md Al Amin', 1500)

user_1.setBalance(1500)
print(user_1.getBalance())

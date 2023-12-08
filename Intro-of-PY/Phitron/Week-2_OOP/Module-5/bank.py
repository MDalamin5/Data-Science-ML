class Bank:
    def __init__(self,full_name, balance) -> None:
        self.full_name = full_name
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def depostite(self, amount):
        if amount < 0:
            print('Invald amount')
        else:
            self.balance += amount
            print(f"{amount} taka sussfully Dioposite")

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"you have to withdraw more than {self.min_withdraw} taka")
        elif amount >= self.max_withdraw:
            print(f'You can not withdraw more the {self.max_withdraw} taka')
        else:
            if self.balance + 100 > amount:
                self.balance -= amount
                print(f"Here is your amount {amount}\n Thank you!!")
            else:
                print('Not enough amount in your accoutn')

    
dbbl = Bank('Md Al Amin', 100)
dbbl.depostite(500)
# print(alamin.balance)
dbbl.withdraw(1000)



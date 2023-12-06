balence = 3000

def buy_products(items, pirce):
    global balence
    balence = balence - pirce

    return balence

new_bal = buy_products('shirt', 400)
print(new_bal)
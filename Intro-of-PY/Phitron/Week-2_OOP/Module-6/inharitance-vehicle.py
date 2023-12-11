class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def mode(self):
        pass

    def __repr__(self) -> str:
        return f"Name: {self.name}, Ticket Price: {self.price}"


class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        super().__init__(name, price)
        self.seat = seat


    def __repr__(self) -> str:
        return f"Number of seat: {self.seat} {super().__repr__()}"

    


class Truck(Vehicle):
    def __init__(self, name, price, carry_weight) -> None:
        super().__init__(name, price)
        self.cry_weight = carry_weight



class PickupTruck(Truck):
    def __init__(self, name, price, carry_weight) -> None:
        super().__init__(name, price, carry_weight)



class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        super().__init__(name, price, seat)
        self.temperature = temperature



green_line = ACBus('Green Line', 1233, 24, 20)
print(green_line)
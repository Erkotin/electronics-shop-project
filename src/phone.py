from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Unsupported operand type(s) for +: 'Phone' and '{}'".format(type(other).__name__))
        return self.quantity + other.quantity

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

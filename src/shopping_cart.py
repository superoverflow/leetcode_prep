"https://medium.com/@j622amilah/hackerrank-tests-python-3420011863a1"


class Item:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items: list[Item] = []

    def add(self, item: Item) -> None:
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)

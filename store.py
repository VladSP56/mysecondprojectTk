class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"goods {item_name} was added in {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"goods {item_name} deleted from {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"price of goods {item_name} updated in {self.name}")
        else:
            print(f"goods {item_name} wasn't found")

store1 = Store("Bingo", "Nevsky av.35")
store2 = Store("Wow", "Ligovsky pr.43")
store3 = Store("Grand","Lesnoy pr.27")

store1.add_item("bred", 67)
store1.add_item("milk", 120)
store1.add_item('buckwheat', 65)

store1.remove_item("bred")

print(store1.get_price("milk"))

store1.update_price("buckwheat", 80)
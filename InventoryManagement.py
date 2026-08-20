class InventoryManagement:
    def __init__(self):
        self.warehouses = {
            "A": {},
            "B": {},
            "C": {}
        }
        self.suppliers = {}
    def add_product(self, warehouse, product, quantity):
        if quantity <= 0:
            print("Invalid quantity")
            return
        self.warehouses[warehouse][product] = \
            self.warehouses[warehouse].get(product, 0) + quantity
        print(product, "added to Warehouse", warehouse)
    def remove_product(self, warehouse, product, quantity):
        if product not in self.warehouses[warehouse]:
            print("Invalid product")
            return
        if quantity > self.warehouses[warehouse][product]:
            print("Insufficient inventory")
            return
        self.warehouses[warehouse][product] -= quantity
        print(quantity, product, "removed")
    def transfer_stock(self, source, destination, product, quantity):
        if product not in self.warehouses[source]:
            print("Product not found")
            return
        if self.warehouses[source][product] < quantity:
            print("Insufficient stock for transfer")
            return
        self.warehouses[source][product] -= quantity
        self.warehouses[destination][product] = \
            self.warehouses[destination].get(product, 0) + quantity
        print("Stock transferred from", source, "to", destination)
    def add_supplier(self, product, supplier):
        self.suppliers[product] = supplier
    def low_stock(self, limit):
        for w in self.warehouses:
            for product, quantity in self.warehouses[w].items():
                if quantity < limit:
                    print("Low stock:", product, "in Warehouse", w)
    def select_warehouse(self, product, quantity):
        best = None
        highest = 0
        for w in self.warehouses:
            stock = self.warehouses[w].get(product, 0)
            if stock >= quantity and stock > highest:
                highest = stock
                best = w
        if best:
            print("Order should be fulfilled from Warehouse", best)
        else:
            print("Insufficient stock in all warehouses")
    def display(self):
        for w in self.warehouses:
            print("\nWarehouse", w)
            print(self.warehouses[w])
i = InventoryManagement()
i.add_product("A", "Laptop", 10)
i.add_product("B", "Laptop", 25)
i.add_product("C", "Laptop", 5)
i.add_product("A", "Mouse", 100)
i.add_supplier("Laptop", "Dell Supplier")
i.add_supplier("Mouse", "Logitech Supplier")
i.transfer_stock("B", "C", "Laptop", 5)
i.remove_product("A", "Mouse", 10)
i.low_stock(10)
i.select_warehouse("Laptop", 15)
i.display()

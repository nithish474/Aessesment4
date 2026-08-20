import threading


class InventoryManagement:
    def __init__(self):

        self.warehouses = {
            "A": {},
            "B": {},
            "C": {}
        }

        self.suppliers = {}

        self.lock = threading.Lock()

    def add_product(
        self,
        warehouse,
        product,
        quantity
    ):

        with self.lock:

            if warehouse not in self.warehouses:
                print("Invalid warehouse")
                return False

            if quantity <= 0:
                print("Invalid quantity")
                return False

            self.warehouses[warehouse][product] = \
                self.warehouses[warehouse].get(
                    product,
                    0
                ) + quantity

            print(
                product,
                "added to Warehouse",
                warehouse
            )

            return True

    def remove_product(
        self,
        warehouse,
        product,
        quantity
    ):

        with self.lock:

            if warehouse not in self.warehouses:
                print("Invalid warehouse")
                return False

            if quantity <= 0:
                print("Invalid quantity")
                return False

            if product not in self.warehouses[warehouse]:
                print("Invalid product")
                return False

            if quantity > self.warehouses[warehouse][product]:
                print("Insufficient inventory")
                return False

            self.warehouses[warehouse][product] -= quantity

            print(
                quantity,
                product,
                "removed"
            )

            return True

    def transfer_stock(
        self,
        source,
        destination,
        product,
        quantity
    ):

        with self.lock:

            if source not in self.warehouses:
                print("Invalid source warehouse")
                return False

            if destination not in self.warehouses:
                print("Invalid destination warehouse")
                return False

            if quantity <= 0:
                print("Invalid quantity")
                return False

            if product not in self.warehouses[source]:
                print("Product not found")
                return False

            if self.warehouses[source][product] < quantity:
                print("Insufficient stock for transfer")
                return False

            self.warehouses[source][product] -= quantity

            self.warehouses[destination][product] = \
                self.warehouses[destination].get(
                    product,
                    0
                ) + quantity

            print(
                "Stock transferred from",
                source,
                "to",
                destination
            )

            return True

    def add_supplier(
        self,
        product,
        supplier
    ):

        self.suppliers[product] = supplier

        print(
            "Supplier added:",
            supplier
        )

    def reorder(self, warehouse, product, quantity):

        if product not in self.suppliers:
            print("No supplier available")
            return False

        print(
            "Reorder placed for",
            product,
            "Quantity:",
            quantity,
            "Supplier:",
            self.suppliers[product]
        )

        return True

    def low_stock(self, limit):

        for w in self.warehouses:

            for product, quantity in \
                    self.warehouses[w].items():

                if quantity < limit:

                    print(
                        "Low stock:",
                        product,
                        "in Warehouse",
                        w
                    )

    def select_warehouse(
        self,
        product,
        quantity
    ):

        best = None
        highest = 0

        for w in self.warehouses:

            stock = self.warehouses[w].get(
                product,
                0
            )

            if stock >= quantity and stock > highest:

                highest = stock
                best = w

        if best:

            print(
                "Order should be fulfilled from Warehouse",
                best
            )

            return best

        else:

            print(
                "Insufficient stock in all warehouses"
            )

            return None

    def display(self):

        for w in self.warehouses:

            print("\nWarehouse", w)

            print(
                self.warehouses[w]
            )


if __name__ == "__main__":

    i = InventoryManagement()

    i.add_product(
        "A",
        "Laptop",
        10
    )

    i.add_product(
        "B",
        "Laptop",
        25
    )

    i.add_product(
        "C",
        "Laptop",
        5
    )

    i.add_product(
        "A",
        "Mouse",
        100
    )

    i.add_supplier(
        "Laptop",
        "Dell Supplier"
    )

    i.add_supplier(
        "Mouse",
        "Logitech Supplier"
    )

    i.transfer_stock(
        "B",
        "C",
        "Laptop",
        5
    )

    i.remove_product(
        "A",
        "Mouse",
        10
    )

    i.low_stock(10)

    i.select_warehouse(
        "Laptop",
        15
    )

    i.display()

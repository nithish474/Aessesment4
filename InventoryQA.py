from InventoryManagement import InventoryManagement
import threading


print("===== INVENTORY QA =====")

i = InventoryManagement()


# Test 1
print("\nTest 1: Stock Availability")

i.add_product(
    "A",
    "Laptop",
    20
)

i.remove_product(
    "A",
    "Laptop",
    5
)


# Test 2
print("\nTest 2: Insufficient Inventory")

i.remove_product(
    "A",
    "Laptop",
    100
)


# Test 3
print("\nTest 3: Warehouse Transfer")

i.transfer_stock(
    "A",
    "B",
    "Laptop",
    10
)


# Test 4
print("\nTest 4: Reorder Threshold")

i.add_supplier(
    "Laptop",
    "Dell Supplier"
)

i.low_stock(15)

i.reorder(
    "A",
    "Laptop",
    50
)


# Test 5
print("\nTest 5: Invalid Product")

i.remove_product(
    "A",
    "Phone",
    5
)


# Test 6
print("\nTest 6: Negative Inventory")

i.add_product(
    "A",
    "Mouse",
    -10
)


# Test 7
print("\nTest 7: Multiple Warehouses")

i.add_product(
    "A",
    "Keyboard",
    10
)

i.add_product(
    "B",
    "Keyboard",
    30
)

i.add_product(
    "C",
    "Keyboard",
    5
)

i.select_warehouse(
    "Keyboard",
    15
)


# Test 8
print("\nTest 8: Concurrent Orders")

i.add_product(
    "A",
    "Mouse",
    10
)


def order():
    i.remove_product(
        "A",
        "Mouse",
        6
    )


t1 = threading.Thread(
    target=order
)

t2 = threading.Thread(
    target=order
)

t1.start()
t2.start()

t1.join()
t2.join()

i.display()

print("\n===== QA COMPLETED =====")

from DigitalWallet import DigitalWallet
import threading


print("===== DIGITAL WALLET QA =====")

w = DigitalWallet()


# Test 1
print("\nTest 1: Normal Transaction")

w.create_account("User1", 1234, 10000)
w.create_account("User2", 5678, 5000)

w.deposit("User1", 2000)

w.withdraw(
    "User1",
    1234,
    1000
)


# Test 2
print("\nTest 2: Insufficient Balance")

w.withdraw(
    "User1",
    1234,
    50000
)


# Test 3
print("\nTest 3: Negative Amount")

w.deposit(
    "User1",
    -1000
)


# Test 4
print("\nTest 4: Multiple Failed PINs")

w.withdraw("User1", 1111, 100)
w.withdraw("User1", 2222, 100)
w.withdraw("User1", 3333, 100)


# Test 5
print("\nTest 5: Daily Limit")

w.withdraw(
    "User1",
    1234,
    50000
)

w.withdraw(
    "User1",
    1234,
    60000
)


# Test 6
print("\nTest 6: Suspicious Large Transaction")

w.deposit(
    "User1",
    100000
)

w.withdraw(
    "User1",
    1234,
    60000
)


# Test 7
print("\nTest 7: Duplicate Account")

w.create_account(
    "User1",
    1234,
    5000
)


# Test 8
print("\nTest 8: Concurrent Transactions")

w.create_account(
    "User3",
    9999,
    10000
)


def transaction():
    w.withdraw(
        "User3",
        9999,
        1000
    )


t1 = threading.Thread(
    target=transaction
)

t2 = threading.Thread(
    target=transaction
)

t1.start()
t2.start()

t1.join()
t2.join()

w.show_balance("User3")

print("\n===== QA COMPLETED =====")

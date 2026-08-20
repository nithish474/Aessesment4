from datetime import datetime, timedelta
import threading


class DigitalWallet:
    def __init__(self):
        self.accounts = {}
        self.history = []
        self.lock = threading.Lock()

    def create_account(self, user, pin, balance=0):
        with self.lock:
            if user in self.accounts:
                print("Account already exists")
                return False

            if balance < 0:
                print("Invalid balance")
                return False

            self.accounts[user] = {
                "pin": pin,
                "balance": balance,
                "daily_amount": 0,
                "failed_pin": 0
            }

            print("Account created:", user)
            return True

    def check_pin(self, user, pin):
        if user not in self.accounts:
            print("Account not found")
            return False

        if self.accounts[user]["pin"] != pin:
            self.accounts[user]["failed_pin"] += 1

            if self.accounts[user]["failed_pin"] >= 3:
                print("Suspicious: Multiple failed PIN attempts")

            return False

        self.accounts[user]["failed_pin"] = 0
        return True

    def fraud_check(self, user, amount):
        now = datetime.now()

        recent = []

        for x in self.history:
            if x["user"] == user:
                if now - x["time"] <= timedelta(minutes=10):
                    recent.append(x)

        if len(recent) >= 5:
            print("Suspicious: More than 5 transactions in 10 minutes")

        if amount > 50000:
            print("Suspicious: Large transaction")

        if amount > 10000 and amount % 1000 != 0:
            print("Suspicious: Unusual transaction amount")

    def add_history(self, user, transaction_type, amount):
        self.history.append({
            "user": user,
            "type": transaction_type,
            "amount": amount,
            "time": datetime.now()
        })

    def deposit(self, user, amount):
        with self.lock:
            if user not in self.accounts:
                print("Account not found")
                return False

            if amount <= 0:
                print("Invalid amount")
                return False

            self.accounts[user]["balance"] += amount

            self.add_history(user, "Deposit", amount)

            print("Deposited:", amount)
            return True

    def withdraw(self, user, pin, amount):
        with self.lock:
            if user not in self.accounts:
                print("Account not found")
                return False

            if not self.check_pin(user, pin):
                print("Wrong PIN")
                return False

            if amount <= 0:
                print("Invalid amount")
                return False

            if amount > self.accounts[user]["balance"]:
                print("Insufficient balance")
                return False

            if self.accounts[user]["daily_amount"] + amount > 100000:
                print("Daily transaction limit exceeded")
                return False

            self.fraud_check(user, amount)

            self.accounts[user]["balance"] -= amount
            self.accounts[user]["daily_amount"] += amount

            self.add_history(user, "Withdrawal", amount)

            print("Withdrawal successful")
            return True

    def transfer(self, sender, receiver, pin, amount):
        with self.lock:
            if sender not in self.accounts:
                print("Sender not found")
                return False

            if receiver not in self.accounts:
                print("Receiver not found")
                return False

            if sender == receiver:
                print("Cannot transfer to same account")
                return False

            if not self.check_pin(sender, pin):
                print("Wrong PIN")
                return False

            if amount <= 0:
                print("Invalid amount")
                return False

            if amount > self.accounts[sender]["balance"]:
                print("Insufficient balance")
                return False

            if self.accounts[sender]["daily_amount"] + amount > 100000:
                print("Daily transaction limit exceeded")
                return False

            self.fraud_check(sender, amount)

            self.accounts[sender]["balance"] -= amount
            self.accounts[receiver]["balance"] += amount
            self.accounts[sender]["daily_amount"] += amount

            self.add_history(sender, "Transfer", amount)

            print("Transfer successful")
            return True

    def show_balance(self, user):
        if user in self.accounts:
            print(user, "Balance:", self.accounts[user]["balance"])

    def show_history(self):
        for x in self.history:
            print(
                x["user"],
                x["type"],
                x["amount"]
            )


if __name__ == "__main__":

    w = DigitalWallet()

    w.create_account("Nithish", 1234, 100000)
    w.create_account("Rahul", 5678, 50000)

    w.deposit("Nithish", 5000)
    w.withdraw("Nithish", 1234, 10000)

    w.transfer(
        "Nithish",
        "Rahul",
        1234,
        20000
    )

    w.show_balance("Nithish")
    w.show_balance("Rahul")

    print("\nTransaction History")
    w.show_history()

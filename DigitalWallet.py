from datetime import datetime, timedelta
class DigitalWallet:
    def __init__(self):
        self.accounts = {}
        self.history = []
    def create_account(self, user, pin, balance=0):
        if user in self.accounts:
            print("Account already exists")
            return
        self.accounts[user] = {
            "pin": pin,
            "balance": balance,
            "daily_amount": 0,
            "failed_pin": 0
        }
        print("Account created:", user)
    def check_pin(self, user, pin):
        if self.accounts[user]["pin"] != pin:
            self.accounts[user]["failed_pin"] += 1
            if self.accounts[user]["failed_pin"] >= 3:
                print("Suspicious: Multiple failed PIN attempts")
            return False
        self.accounts[user]["failed_pin"] = 0
        return True
    def fraud_check(self, user, amount):
        now = datetime.now()
        recent = [
            x for x in self.history
            if x["user"] == user and
            now - x["time"] <= timedelta(minutes=10)
        ]
        if len(recent) >= 5:
            print("Suspicious: More than 5 transactions in 10 minutes")
        if amount > 50000:
            print("Suspicious: Large transaction")
        if amount % 1000 != 0 and amount > 10000:
            print("Suspicious: Unusual transaction amount")
    def deposit(self, user, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.accounts[user]["balance"] += amount
        self.history.append({
            "user": user,
            "type": "Deposit",
            "amount": amount,
            "time": datetime.now()
        })
        print("Deposited:", amount)
    def withdraw(self, user, pin, amount):
        if not self.check_pin(user, pin):
            print("Wrong PIN")
            return
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.accounts[user]["balance"]:
            print("Insufficient balance")
            return
        if self.accounts[user]["daily_amount"] + amount > 100000:
            print("Daily transaction limit exceeded")
            return
        self.fraud_check(user, amount)
        self.accounts[user]["balance"] -= amount
        self.accounts[user]["daily_amount"] += amount
        self.history.append({
            "user": user,
            "type": "Withdrawal",
            "amount": amount,
            "time": datetime.now()
        })
        print("Withdrawal successful")
    def transfer(self, sender, receiver, pin, amount):
        if receiver not in self.accounts:
            print("Receiver not found")
            return
        if not self.check_pin(sender, pin):
            print("Wrong PIN")
            return
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.accounts[sender]["balance"]:
            print("Insufficient balance")
            return
        if self.accounts[sender]["daily_amount"] + amount > 100000:
            print("Daily limit exceeded")
            return
        self.fraud_check(sender, amount)
        self.accounts[sender]["balance"] -= amount
        self.accounts[receiver]["balance"] += amount
        self.accounts[sender]["daily_amount"] += amount
        self.history.append({
            "user": sender,
            "type": "Transfer",
            "amount": amount,
            "time": datetime.now()
        })
        print("Transfer successful")
    def show_balance(self, user):
        print(user, "Balance:", self.accounts[user]["balance"])
    def show_history(self):
        for x in self.history:
            print(x["user"], x["type"], x["amount"])
w = DigitalWallet()
w.create_account("Nithish", 1234, 100000)
w.create_account("Rahul", 5678, 50000)
w.deposit("Nithish", 5000)
w.withdraw("Nithish", 1234, 10000)
w.transfer("Nithish", "Rahul", 1234, 20000)
w.show_balance("Nithish")
w.show_balance("Rahul")
print("\nTransaction History")
w.show_history()

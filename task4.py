import threading
import random
from collections import defaultdict

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew: {amount}, New Balance: {self.balance}")
            else:
                print(f"Withdrawal of {amount} failed, Insufficient funds. Current Balance: {self.balance}")

def client(account):
    for _ in range(10):
        action = random.choice(['deposit', 'withdraw'])
        amount = random.randint(1, 100)
        if action == 'deposit':
            account.deposit(amount)
        else:
            account.withdraw(amount)

if __name__ == "__main__":
    account = BankAccount()
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=client, args=(account,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final account balance:", account.balance)
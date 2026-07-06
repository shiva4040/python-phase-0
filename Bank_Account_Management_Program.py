class BankAccount :
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def show(self):
        print(f"Your current balance : {self.balance}")
    def deposit(self,amount):
        if amount < 0:
            self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")
per1 = BankAccount("Shiva",20000)
per1.show()
# Deposit
while True:
    check1 = input("You want to deposit money (yes/no) : ").lower()
    if check1 =="yes" :
        deposit_money = int(input("Enter your money to deposit : "))
        while True:
            if deposit_money > 0 :
                per1.deposit(deposit_money)
                print("Money deposited successfully!")
                per1.show()
                break
            else:
                print("Enter valid amount")
                break
    elif check1 == "no":
        per1.show()
        break
    else:
        print("wrong choice choose only (yes/no)")
# Wihtdraw
while True:
    check1 = input("You want to withdraw money (yes/no) : ").lower()
    if check1 =="yes" :
        withdraw_money = int(input("Enter your money to withdraw : "))
        per1.withdraw(withdraw_money)
        per1.show()
        break
    elif check1 == "no":
        per1.show()
        break
    else:
        print("wrong choice choose only (yes/no)")

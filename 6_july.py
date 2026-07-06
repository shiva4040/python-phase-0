# n = int(input("How many name you want to add : "))

# info = []
# for i in range(n):
#     person = input("Enter name : ")
#     class data :
#         def __init__ (self,name):
#             print("hello",name)
#             info.append(name)       
#     data(person)

# print(info)

# class info :
#     def __init__ (self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city
# s1 = info("Shiva",18,"shahijan")
# print(s1.name)

# class car :
#     def __init__ (self,brand,color):
#         self.brand = brand
#         self.color = color
#     def start(self):
#             print(f"{self.brand} is starting")
#     def detail(self):
#             print(f"Brand :{self.brand}")
#             print(f"Color : {self.color}")
# c1 = car("BMW","Black")
# c2 = car("Bugati","Red")
# c1.start()
# c1.detail()
# print()
# c2.start()
# c2.detail()

class BankAccount :
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def show(self):
        print(f"total balance : {self.balance}")
per1 = BankAccount("Shiva",12000)
per1.deposit(2000)
per1.withdraw(400)
print()
per1.show()
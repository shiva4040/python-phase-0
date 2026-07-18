import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os
month = input("Enter month :")
category = input("Enter category : ")
discription = input("Enter discripion : ")
amount = int(input("Enter amount : "))
data = {
    "month" : [month],
    "category" : [category],
    "discription" : [discription],
    "amount" : [amount]
}
df1 = pd.DataFrame(data)
file_exist = os.path.exists("expenses.csv")
df1.to_csv("expenses.csv" , mode = "a", header = not file_exist,index = False)

# view

df = pd.read_csv("expenses.csv")
print(df.head())

# filter 

r = df.groupby(["category", "month"])["amount"].sum().reset_index()
cat = input("Enter category to filter : ")
filtered = df[df["category"] == cat]
print(filtered)

# plot chart

sns.barplot(x = r["month"] , y = r["amount"])
plt.xlabel("Month")
plt.ylabel("Amount")
plt.show()
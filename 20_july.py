import random
import matplotlib.pyplot as plt
#random variable
x = random.randint(1,6)
print(x)

#probability Distribution

# roll = {
#     1 :0,
#     2 :0,
#     3 :0,
#     4 :0,
#     5 :0,
#     6 :0,
# }
# for i in range(10000):
#     r = random.randint(1,6)
#     roll[r] += 1
# print(roll)

roll = [random.randint(1,6) for _ in range(10000)]
count ={}
for i in roll:
    count[i]= count.get(i,0)+1
for i, j in count.items():
    print(i,j/10000)
mean = sum(roll)/len(roll)
print("mean: ",mean)

# plot

plt.bar(count.keys(), count.values() )
plt.title("Distribution of 10,000 Dice Rolls")
plt.xlabel("keys")
plt.ylabel("values")
plt.grid(axis='y')
plt.show()


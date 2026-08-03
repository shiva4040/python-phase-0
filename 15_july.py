v1 = [2,1]
v2 = [3,3]
#addition
a =[]
for i in range(len(v1)):
    a.append(v1[i] + v2[i])
print(a)

# Multiplication
cost = 0
for i in range(len(v1)):
    cost += v1[i] * v2[i]
print(cost)

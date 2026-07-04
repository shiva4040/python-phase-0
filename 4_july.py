# #List creation

# list = [1,2,3,4,5,5,6,7,"Shiva","Age"]
# # print(list)

# # indexing

# print(list[1])
# print(list[4]) # list[index_number]
# print(list[-2])

# print(list[0:5]) # list[start : stop : step]
# print(list[2:])
# print(list[0: :2])
# print(list[1:5:3])
# print(list[0::])
# print(list[::-1]) # for revers

# # Append

# list.append(3)
# list.append([2,34,5,5])
# list.append("name")
# print(list)

# # pop

# list.pop() #remove from end
# list.pop(2) #remove by index
# print(list)

# #  List Comprehensions

# #  without List Comprehensions

# empty = []

# for i in range(1,11):
#     empty.append(i)
# print(empty)

# # With  List Comprehensions

# # [new_item or output for item in iterable] 

# square = [i for i in range(1,11)]
# print(square)

# even = [i for i in range(1,11) if (i %2 == 0)]
# print(even)

# names = ["shiva", "aman", "rahul"]
# upper = [i.upper() for i in names ]
# print(upper)


# words = ["apple", "banana", "cat"]
# length = [len(i) for i in words]
# print(length)



 # Mini: Student grade manager — store names+marks in a list, print top scorer.
 
name = input("Enter your name : ")
score =[] 
for i in range(1,6):
    result = int(input(f"Enter your subject{i} marks : "))
    score.append(result)
print(f"Your final score : {score}")
top = max(score)
ind = score.index(top)
print(f"Your heighest marks is {top} in subject {ind +1} ")

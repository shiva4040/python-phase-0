# with open("a.txt","w") as file :
#     file.write("my name is shiva")
# with open("a.txt","r") as file :
#     read = file.read()
# print(read)

# import csv
# with open("a.csv","w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name,age ,marks"])
#     writer.writerow(["Shiva",18,580])
#     writer.writerow(["Shivam",22,880])
#     writer.writerow(["Shubham",14,680])
# with open ("a.csv","r",newline="") as file:
#     reader = csv.reader(file)
#     for r in reader:
#         print(r)
# data = []
# with open("a.txt","r") as file :
#     read = file.read()
#     word = read.split()
#     for i in word :
#         l = len(i)
#         data.append(l)
# data.sort()
# print(data)
# final = data[::-1]
# new = final[:5]
# print(new)

with open("a.txt","r") as file:
    read = file.read()
    split = read.split()
    count = {}
    for i in split:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for word, freq in result[:5]:
        print(word, ":", freq)
   
        
import itertools
import csv

# def add(n):
#     for i in range(n):
#         yield i+1
    
# x = add(50)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# for i in range(34):
#     print(next(x))

# x = itertools.count(1)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# for i in range(1000):
#     print(next(x))

# y = itertools.cycle([1,2,3,4,3,5])
# for i in range(100):
#     print(next(y)

# a = [2,3,4,5,3,2,2]
# b = ["afa","afaa","aferer","fgrrgf"]
# z = itertools.chain(a,b)
# for i in z:
#     print(i)

# x = itertools.count()
# result = itertools.islice(x,5)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# Mini: Implement a data batch generator — yield batches of 32 rows from a CSV.

def batch_generator(file_name,batch_size = 32):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        batch = []
        for row in reader:
            batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
        if batch:
            yield batch
generator = batch_generator("Titanic-Dataset.csv")
batch1 = next(generator)
print("batch size : ",len(batch1))
# print(batch1)

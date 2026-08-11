import random
# result = [x for x in range(5)]
# print(result)
# square = [x**2 for x in range(1,25)]
# print(square)

result = [x for x in range(1,6) if x%2 == 0]
print(result)
value = ["even" if x%2 == 0 else "odd" for x in range(1,100)]
# print(value)
# even =0
# odd =0
# for i in value:
#     if i == "even":
#         even +=1
#     else:
#         odd +=1
# print(even)
# print(odd)

# even = len([x for x in value if x == "even"])
# odd = len([x for x in value if x == "odd"])
# print(even)
# print(odd)

# square = {x : x**2 for x in range(1,11)}
# print(square)

# result = {x:"even" if x%2 == 0 else "odd" for x in range(1,11)}
# print(result)
# matrix = [[i*j for i in range(1,6)] for j in range(1,6)]
# for row in matrix:
#     print(row, "\n")

# mini: Rewrite a 20-line loop-based function using comprehensions.
def proces_number(number):
    result ={x : "pass" if x >=40 else "Fail" for x in number}
    square = {x: x**2 for x in number}
    even_odd = ["even" if x%2==0 else "odd" for x in number]
    return result ,square,even_odd
number = random.sample([x for x in range(1,101)],25)
print(*proces_number(number) ,sep="\n \n \n")

# Dictionary CRUD
# creation

dict ={
    "id" : 1,
    "name" : "Shiva",
    "age" : 18
}
# print(dict)
# print(dict["id"])

# # read

# print(dict["name"])
# print(dict.get("name"))

# # update

# dict["age"] = 19
# dict["city"] = "robertsganj"
# print(dict)

# # deletion
 
# del dict["age"]
# dict.pop("name")
# print(dict)


# print(dict.values())
# print(dict.items())
# print(dict.keys())

# loops
# for keys in dict :
#     print(keys ,":", dict[keys])

# for key ,value in dict.items() :
#     print( key, ":",value )
    
    
# # Nested dictionary

# data = {
#     "stu_1" : {
#         "name" : "Shiva",
#         "age" : 18,
#         "grade" : "A"
#     },
#     "stu_2" : {
#         "name" : "Shivam",
#         "age" : 22,
#         "grade" : "A"
#     },
#     "stu_3" : {
#         "name" : "Shubham",
#         "age" : 14,
#         "grade" : "A"
#     }
    
# }
# print(data.get("stu_1"))
# print(data["stu_1"]["name"])
# data["stu_2"]["grade"] = "A+"
# print(data["stu_2"]["grade"])

# for key , value in data.items() :
#     print("data : ", key)
#     for keys , values in value.items() :
#         print(keys ,":", values)


# person = ( "Shiva",18,"up")
# name, age , city = person 
# print(name)
# print(age)
# print(city)

# #swape
# a=1
# b= 2
# a , b = b , a

# print(a)
# print(b)

# name , _ , city = person #( _ )is commonly used for values you don't need.
# print(name)
# print(city)

# num = (1,2,3,4,5,6,7,8)

# first ,*middle , last =num
# print(first)
# print(middle)
# print(last)


# Mini: Phonebook app — add, search, delete contacts stored in a dict.

phonebook = {}


# Added

n = int(input("how many number you want to add : "))
for i in range(n):
    name = input("Enter your name : ")
    number = int(input("Enter your number : "))
    phonebook[name] = number
    print(f"{name} Added successfully!")
    
# Search 

person = input("Enter your name to find : ")
found = False
for key,vlaue in phonebook.items():
    if (key == person):
        print(f"{key}'s Number : {phonebook[key]}")
        found = True
        break
if not found:
        print("number is no exist in phonebook")

# Store data

print("--- Contact List ---")
for keys,vlaues in phonebook.items():
    print(keys ,":",phonebook[keys])
        
# Deletion

found = False
delete = int(input("Enter your number to delete : "))
for key,vlaue in phonebook.items():
    if (vlaue == delete):
        print(f"{key} :{phonebook[key]} is deleted ")
        del phonebook[key]
        found = True
        break
if not found:
        print("number is no exist in phonebook")

# final
        
print("--- Contact List ---")
for keys,vlaues in phonebook.items():
    print(keys ,":",phonebook[keys])
        
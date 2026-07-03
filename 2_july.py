# num = 2
# if num > 5 :
#     print("large number")
# else:
#     print("small number")

#FizzBuzz is a classic beginner programming exercise
# The rules

# Print the numbers from 1 to 100, but:

# If a number is divisible by 3, print "Fizz".
# If a number is divisible by 5, print "Buzz".
# If a number is divisible by both 3 and 5, print "FizzBuzz".
# Otherwise, print the number itself.

for i in range(1,101):
    if(i%3 == 0 and i%5 ==0):
        print("FizzBuzz") 
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)

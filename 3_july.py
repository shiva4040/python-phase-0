num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Enter oprator : ")

def calculator (i,j,opt):
    if (opt == "+") :
        return print("result : ",i+j)
    elif (opt == "-") :
        return print("result : ",i-j)
    elif (opt == "*") :
        return print("result : ",i*j)
    elif (opt == "/") :
        return print("result : ",i/j)
    else:
        return print("wrong oprator")


calculator(num1,num2,op)
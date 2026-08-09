import time
def add(*args):
    total =0
    for i in args:
        total +=i
    return args,"=",total
print(add(2,4,5,2))

def stu(**kwargs):
    return kwargs
print(stu(name = "Shiva",age = 20,branch = "CSE"))
print(stu(a = 11))
#closure
def make_up(lr):
    def update(w,grad):
        return w-lr*grad
    return update
fast = make_up(0.1)
print(fast(10,4))
#decorator
def dect(fun):
    def mfx():
        print("hello")
        fun()
        print("code end")
    return mfx
@dect
def name():
    print("shiva")    
name()

# Mini: Write a @timer decorator that prints how long any function takes.
def time_taken(fun):
    def mfx(*args, **kwargs):
        start = time.time()
        fun(*args,**kwargs)
        end = time.time()
        print("Total time taken : ", end-start)
    return mfx
@time_taken
def work():
    for i in range(10000):
        i +=1
        print(i)
work()
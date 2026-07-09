import numpy as np
arr = np.array([[1,3,45,6,66],[3,4342,2312,31,313]])
# print(arr)
# print(arr.shape)
# print(arr.dtype)
# print(arr[1,4])
# print(arr[:2,:3])
# print(np.arange(1,5))
# print(np.zeros([2,5]))
# print(np.ones([4,5]))
# print(np.linspace(1,20,3))
# print(np.zeros([5,5]))


# Mini: Create a 5×5 matrix. Compute row sums and column means.
    
a = np.arange(1,26).reshape(5,5)
sum = np.sum(a,axis=1)
mean = np.mean(a,axis = 0)
print(a)
print ("sum : ",sum)
print("mean : ",mean)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# mat1 = [[1,2],
#         [4,5]]
# mat2 = [[6,2],
#         [2,4]]
# a = (mat1[0][0]*mat1[1][1] )-(mat1[0][1]*mat1[1][0])
# print(a)

# A = np.array([[5,2],
#             [7,1]])
# print(np.linalg.det(A))
# values,vector = np.linalg.eig(A)
# print(values)
# print(vector)

s = np.array([[3,4,5],
             [2,5,7],
             [4,6,2]])
value, vector = np.linalg.eig(s)
print(value)
print(vector)

# Mini: Use NumPy to find eigenvalues of a 3×3 matrix. Visualize with matplotlib.

sns.barplot(
    x=["λ1", "λ2", "λ3"],
    y=value.real
)
plt.title("Eigenvalues of a 3×3 Matrix")
plt.xlabel("Eigenvalues")
plt.ylabel("Value")
plt.grid(True)
plt.show()
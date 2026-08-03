# m1 = [[1,2,3],
#       [3,4,5]]
# v = [3,5,4]
# r = []
# for row in m1 :
#     total = 0
#     for i in range(len(v)):
#         total += row[i] * v[i]
#     r.append(total)
# print(r)

# Mini: Implement 2×2 matrix multiply from scratch.
mat1 = [[1,2],
        [1,6]]
mat2 = [[4,5],
        [6,5]]
r = [[0,0],
     [0,0]]
for i in range(2):
    for j in range(2):
        r[i][j] = 0
        for k in range(2):
            r[i][j] += mat1[i][k] * mat2[k][j]
for f in r:
    print(f)
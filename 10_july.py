# Mini: Implement dot product from scratch, then verify with np.dot().
import numpy as np
c = np.arange(1,6).reshape(5)
d = np.arange(1,6).reshape(5)
dot = 0
for i in range(len(c)):
    dot += c[i]*d[i]
print(f"Dot Product (Manual): {dot}")
print(f"Dot Product (np.dot): {np.dot(c,d)}")
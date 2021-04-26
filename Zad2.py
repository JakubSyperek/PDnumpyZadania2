import numpy as np
a = np.array([[2,5,7],[6,4,4],[12,6,2]])
b = np.array([[1,4,1,5],[9,2,6,5],[3,5,8,9],[7,9,3,2]])

print(a.min(axis=1))
print(b.min(axis=1))
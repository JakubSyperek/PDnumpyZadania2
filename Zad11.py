import numpy as np

a = np.arange(1, 25, 2)
print(a)
b1 = a.reshape(3,4)
print(b1)
b2 = a.reshape(4,3)
print(b2)
b3 = a.reshape(2,6)
print(b3)

c1 = b1.flatten()
c2 = b2.flatten()
c3 = b3.flatten()
print(c1)
print(c2)
print(c3)
#Tak, są.
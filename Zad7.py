import numpy as np

def macierze(x1,y1,z1,t1,u1,v1,x2,y2,z2,t2,u2,v2):
    a = np.sin(np.array([[x1, y1, z1], [t1, u1, v1]]))
    b = np.cos(np.array([[x2, y2, z2], [t2, u2, v2]]))
    x = a+b
    print(x)

macierze(4,3,7,2,8,5,2,12,6,9,9,7)

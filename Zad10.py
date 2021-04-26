import numpy as np

a = np.zeros((9,9))
print(a)
b = a.reshape((27,3))
print(b)

#Wymiary tej macierzy można zmienić tylko do 1x81, 3x27, 27x3 i 81x1, czyli wymiary złożone z dzielników liczby 81.
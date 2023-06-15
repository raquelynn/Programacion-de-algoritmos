import numpy as np
lista=["hola",123,123]
lista2=[13,12,11]
matriz=np.array(lista)
matriz2=np.array(lista2)
lista.append(1313)
print(matriz2)
np.append(matriz,matriz2,axis=0)
print(lista)
print(matriz)
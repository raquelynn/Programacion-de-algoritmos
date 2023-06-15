import numpy as np
matriz=np.arange(1,101).reshape(10,10);
print(matriz);
'''
def num_asiento():
    fila=int(input("Fila del asiento:\n"));
    columna=int(input("Columna del asiento:\n"));
    for i in range(fila):
        for j in range(columna):
            asiento_seleccionado=matriz[i,j];
    print(asiento_seleccionado);

matriz_vacia=np.empty((10,10),dtype=object);
print(type(matriz_vacia));
asiento=0;
for fila in range(10):
    for columna in range(10):
        asiento=asiento+1;
        matriz_vacia[fila,columna]=asiento;

print(type(matriz_vacia));'''

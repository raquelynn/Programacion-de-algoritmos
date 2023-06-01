'''1.1 crear un arreglo unidimensional de tamaño 10, com elementos aleatorios de numeros enteros del 0 al 100,
para ello debera investigar la funcion que permita crear numeros aleatorios
1.2 crear una copia del arreglo y muestre
elemento mayor
elemento menor
suma de los elementos
promedio de los elementos
mostrar todos los elementos'''
import random
import numpy as np
arreglo=np.random.randint(100, size = (10));
menor=min(arreglo);
mayor=max(arreglo);
suma=sum(arreglo);
largo=len(arreglo);
promedio=suma/largo;
print(f"El arreglo aleatorio es \n{arreglo}");
print(f"El elemento mayor es \n\t{mayor}");
print(f"El elemento menor es \n\t{menor}");
print(f"La suma de los elementos es \n\t{suma}");
print(f"El promedio de los elementos es \n\t{promedio}");
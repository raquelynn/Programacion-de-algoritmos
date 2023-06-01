#ejercicio 5:ingrese 3 numeros enteros, si son mayores a cero y par, entonces sumelos, sino cuentelos
print("Ingrese 3 numeros enteros");#el punto y coma no es necesario pero el profesor siempre lo pone
num1=int(input())
num2=int(input())
num3=int(input())
suma=0
contador=0
if num1>0 and num1%2==0:
    suma=suma+num1
else:
    contador=contador+1
if num2>0 and num2%2==0:
    suma=suma+num2
else:
    contador=contador+1
if num3>0 and num3%2==0:
    suma=suma+num3
else:
    contador=contador+1
    
print("La suma de los numeros positivos y pares es: ",suma," y la cantidad de numeros que no son positivos y pares son: ",contador)
 
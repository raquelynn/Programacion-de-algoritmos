#numero mayor: ingrese por teclado 2 numeros enteros e indique cual de ellos es mayor
num1=int(input("ingrese un numero\n"));
num2=int(input("ingrese otro numero\n"));
if num1>num2:
    print(num1," es mayor que ",num2);
elif num1==num2:
    print(num1," es igual a ",num2);
else:
    print(num1," es menor a ",num2);
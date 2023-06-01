#par_impar: ingrese un numero entero mayor a 1 y menor a 101 por teclado, luego indique si es par o impar
num=int(input("Ingrese un numero entero mayor a 1 y menor a 101\n"));
if num<=1 or num>=101:
    print("El numero ingresado no esta en el rango pedido");
else:
    if num%2==0:
        print("El numero es par");
    else:
        print("El numero es impar");
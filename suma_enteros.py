#suma_enteros:ingrese por teclado 2 numeros enteros positivos, sumelos y entregue su resultado
num1=int(input("Ingrese un numero entero positivo\n"))
num2=int(input("Ingrese otro numero entero positivo\n"))
if num1<0 or num2<0:
    print("ambos numeros deben ser enteros y positivos")

else:
    resultado=num1+num2
    print(num1,"+",num2,"=",resultado)
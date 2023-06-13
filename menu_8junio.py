from funciones import *
flag=True
print("Bienvenido");
while flag:
    print("~~~~~~Menu~~~~~~");
    print("(1) Calcular iva");
    print("(2) Calcular descuento");
    print("(3) Calcular imc");
    try:
        opcion=int(input(""));
        if opcion==1:
            calcular_iva(int(input("Ingrese el valor para calcular el iva:\n")));
        elif opcion==2:
            descuento(int(input("Ingrese el valor de su producto:\n")),int(input("Ingrese el porcentaje de descuento:\n")));
        elif opcion==3:
            try:
                imc=calcular_imc(float(input("Ingrese su altura:\n")),float(input("Ingrese su peso:\n")));
            except ZeroDivisionError:
                print("Ingrese un valor distinto de 0");
                break
            tabla_imc(float(imc));
    except ValueError:
        print("Ingrese una opcion valida");
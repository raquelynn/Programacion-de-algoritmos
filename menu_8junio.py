from funciones import *
flag=True
while flag:
    print("Bienvenido");
    print("~~~~~~Menu~~~~~~");
    print("(1) Calcular iva");
    print("(2) Calcular descuento");
    print("(3) Calcular imc");
    opcion=int(input(""));
    if opcion==1:
        print("Ingrese el valor para calcular el iva")
        calcular_iva(int(input()));
    elif opcion==2:
        print("Ingrese el valor del producto y el porcentaje de descuento");
        descuento(int(input()),int(input()));
    elif opcion==3:
        print("Ingrese su altura y peso")
        calcular_imc(float(input()),float(input()));
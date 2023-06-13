from funciones import *
print("Bienvenide");
flag=True
while flag:
    menu();
    opcion=int(input("Ingrese una opcion"));
    if opcion==1:
        radio=int(input("Ingrese el radio del circulo\n"));
        area_circ(radio);    
    if opcion==2:
        lado=int(input("Ingrese el lado del cuadrado"));
        perimetro_cuadrado(lado);
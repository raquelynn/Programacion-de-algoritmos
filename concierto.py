import numpy as np
matriz=np.arange(1,101).reshape(10,10);
#print("\n                     Escenario\n");
#print(matriz);
clientes=[];
matrizclientes=np.array(clientes);
while True:
    print("BIenvenido");
    print("1.-Comprar entradas(Maximo 3)");
    print("2.-Mostrar asientos disponibles");
    print("3.-Mostrar asistentes");
    print("4.-Mostrar ganancias");
    print("5.-Salir");
    opcion=int(input("Ingrese una opcion:\n"));
    if opcion==1:
        print("-----compra de entradas-----\n");
        nombre=input("Ingrese su nombre\n");
        rut=int(input("Ingrese su rut sin puntos ni guion:\n"));
        fila=int(input("Fila del asiento:\n"));
        columna=int(input("Columna del asiento:\n"));
        asiento=matriz[fila,columna];
        clientes.append(rut);
        clientes.append(nombre);
        clientes.append(asiento);

        

import numpy as np
matriz=np.arange(1,101,dtype=object).reshape(10,10);
flag1=True;
contador_entradas=0;
total=0;
clientes=[];
opcion=0;
print("\n\tBienvenido <3\n");
#matrizclientes=np.array(clientes);
while flag1:
    flag2=True;
    flag3=True;
    print("\tMENU");
    print("1.-Comprar entradas(Maximo 3)");
    print("2.-Mostrar asientos disponibles");
    print("3.-Mostrar asistentes");
    print("4.-Mostrar ganancias");
    print("5.-Salir");
    try:
        opcion=int(input("\nIngrese una opcion:\n"));
    except ValueError:
        print("Ingrese una opcion valida");
    if opcion==1:
        while flag2:
            print("\n-----Compra de entradas-----\n");
            print("\nValores por asiento:\n1-20          $100.000\n21-60         $50.000\n61-100         $25.000");
            cantidad_ent=int(input("\nIngrese la cantidad de entradas que desea comprar:\n"));
            if cantidad_ent>0 and cantidad_ent<=3:
                while flag3:
                    if cantidad_ent==0:
                        flag3=False;
                        flag2=False;
                    else:
                        fila=int(input("Fila del asiento:\n"));
                        columna=int(input("Columna del asiento:\n"));
                        asiento=matriz[fila,columna];
                        if asiento=='X':
                            print("\nAsiento no disponible!!\n");
                        else:
                            matriz[fila,columna]='X';
                            print(f"Usted ha elegido el asiento {asiento}");
                            nombre=input("Ingrese su nombre\n");
                            rut=int(input("Ingrese su rut sin puntos ni guion:\n"));
                            clientes.append(rut);
                            clientes.append(nombre);
                            clientes.append(asiento);
                            flag2=False;
                            cantidad_ent=cantidad_ent-1;
                            contador_entradas=contador_entradas+1;
                            print(f" te quedan por comprar {cantidad_ent}");
                            if asiento>0 and asiento<=20:
                                total=total+100000;
                            elif asiento>20 and asiento<=60:
                                total=total+50000;
                            else:
                                total=total+25000;
            elif cantidad_ent==0:
                flag2=False;
            else:
                print("Ingrese un valor valido");
    elif opcion==2:
        print("\n        Escenario\n");
        print(matriz);
        print("");
    elif opcion==3:
        print("\n             Asistentes\n");
        matrizclientes=np.array(clientes);
        print(matrizclientes);
        print("");
    elif opcion==4:
        print(f"\nTotal recaudado es ${total}\n");
    elif opcion==5:
        print("...Saliendo del programa, hasta luego...\n");
        flag1=False;

        

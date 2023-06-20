def comprar_entradas(matriz,contador_entradas):
    fila=int(input("Fila del asiento:\n"));
    columna=int(input("Columna del asiento:\n"));
    asiento=matriz[fila,columna];
    matriz[fila,columna]='X';
    print(f"Usted ha elegido el asiento {asiento}");
    contador_entradas=contador_entradas+1
    #print(matriz);
    nombre=input("Ingrese su nombre\n");
    rut=int(input("Ingrese su rut sin puntos ni guion:\n"));
    return matriz,contador_entradas
    return asiento
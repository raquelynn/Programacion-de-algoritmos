#programa que permite iniciar sesion, cambiar cotraseña, cerrar sesion y al realizar 3 intentos de inicio de sesion, te bloquea :o
print("Bienvenid@ al programilla.");
usuario="raquelyn";
contra=1313;
flag1=True;
flag2=True;
bloquear=0;
while flag1:
    print("Que quieres hacer?");
    print("(1)Iniciar sesión");
    print("(2)Cambiar contraseña");
    print("(3)Cerrar programilla");
    opcion=int(input(""));
    if opcion==1:

        while flag2:
            usuario1=str(input("Nombre de usuario:\n"));
            contra1=int(input("Contraseña:\n"));
            if usuario1==usuario and contra1==contra:
                print("Bienvenido Pana Rabit, a la familia.");
                print("Que mas quieres hacer?");
                print("(1)Cambiar contraseña:");
                print("(2)Cerrar sesion");
                opcion=int(input(""));
                if opcion==1:
                    print("cambiando contraseña");
                elif opcion==2:
                    print("Cerrando sesion");
                    flag1=False;
                    flag2=False;
                else:
                    print("Ingrese una opcion correcta");

            else:
                bloquear=bloquear+1
                if bloquear==3:
                    print("Usuario bloqueado");
                    quit()#funcion que sirve para detener el programa
                print("Intente de nuevamente");
            
    elif opcion==2:
        usuario2=str(input("Ingrese su nombre de usuario.\n"));
        contra=int(input("Ingrese su nueva contraseña.\n"));
        print("Nueva contraseña guardada.")
           
    elif opcion==3:
        print("Saliendo del programilla");
        flag1=False;
    else:
        print("Ingrese una opcion correcta");
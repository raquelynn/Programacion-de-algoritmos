print("Bienvenido al servicio de Delivery de nuestra panadería");
try:
    nombre=str(input("Ingrese su nombre:\n"));
    rut=int(input("Ingrese su rut sin digito verificador:\n"));
    dv=int(input("Ingrese el digito verificador:\n"));
except ValueError:
    print("Ingrese un valor válido");
    #return  
#precios
pAmasado=1500;
pMolde=1000;
pBaguette=2000;
pIntegral=3000;
#inicializacion de precio total de cada pan
tAmasado=0;
tBaguette=0;
tIntegral=0;
tMolde=0;
flag=True;
opcion=0;
while flag:
    print("Que desea comprar?");
    print("(1)Pan amasao $1.500");
    print("(2)Pan de Molde $1.000");
    print("(3)Pan Baguette $2.000");
    print("(4)Pan Integral $3.000");
    print("(5)Continuar con el pago");
    try:
        opcion=int(input());
    except ValueError:
        print("Ingrese un valor válido");    
    if opcion==1:
        nAmasado=int(input("Ingrese la cantidad:\n"));
        tAmasado=nAmasado*pAmasado;
    if opcion==2:
        nMolde=int(input("Ingrese la cantidad:\n"));
        tMolde=nMolde*pMolde;
    if opcion==3:
        nBaguette=int(input("Ingrese la cantidad:\n"));
        tBaguette=nBaguette*pBaguette;
    if opcion==4:
        nIntegral=int(input("Ingrese la cantidad:\n"));
        tIntegral=nIntegral*pIntegral;
    if opcion==5:
        flag=False;

total=tAmasado+tMolde+tIntegral+tBaguette
print("-------------------------------");
print("             Boleta            ");
print("");
print(f"Cliente: {nombre}");
print(f"Rut Cliente: {rut}-{dv}");
print("");
if tAmasado>0:
    print(f"Pan amasao          {nAmasado}x$1.500");
if tMolde>0:
    print(f"Pan de Molde        {nMolde}x$1.000");
if tBaguette>0:
    print(f"Pan Baguette        {nBaguette}x$2.000");
if tIntegral>0:
    print(f"Pan Integral        {nIntegral}x$3.000");
print("");
print(f"Total                 ${total}");
print("");
if total<5000:
    deli=total*0.1;
    total=total+deli;
    print(f"El costo de Delivery es {deli}");
else:
    print("Como el total de la compra super los $5.000, el delivery es gratis <3");
    
print(f"Total a pagar ${total}");
print("Gracias por su compra.");
print("-------------------------------");
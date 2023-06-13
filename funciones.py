#funcion sin parametros y sin retorno
def sumar_dos_numeros():
    num1=10;
    num2=9;
    resultado=num1+num2;
    print(f"El resultado de la suma es {resultado}");
#funcion sin parametros u con retorno
def sumar_dos_numeros2():
    num1=10;
    num2=9;
    resultado=num1+num2;
    return resultado;
#con param y sin ret
def sumar_dos_numeros(num1,num2):
    resultado=num1+num2;
    print(f"El resultado de la suma es {resultado}");
#func con param y con ret
def sumar_dos_numeros(num1,num2):
    resultado=num1+num2;
    return resultado
def calcular_iva(precio):
    resultado=precio*0.19;
    print(f"El iva de su producto es {resultado}");
#funcion que calcula el descuento
def descuento(precio,desc):
    desc=desc/100
    precio_final=precio-precio*desc;
    print(f"El precio final con el descuento aplicado es ${precio_final}");
#funcion quecalcula el imc
def calcular_imc(estatura,peso):
    resultado=round(peso/(estatura**2),1);#round redondea con 1 decimal
    return resultado;

#funcion que dice imc
def tabla_imc(imc):
    if imc<18.5:
        print(f"Su imc es {imc} y usted se encuentra bajo peso");
    elif 18.5<=imc and imc<25:
        print(f"Su imc es {imc} y usted se encuentra en peso normal");
    elif 25<=imc and imc<30:
        print(f"Su imc es {imc} y usted tiene sobrepeso");
    elif 30<=imc and imc<35:
        print(f"Su imc es {imc} y usted tiene Obesidad grado 1");
    elif 35<=imc and imc<40:
        print(f"Su imc es {imc} y usted tiene obesidad grado 2");
    else:
        print(f"Su imc es {imc} y usted tiene obesidad grado 3");
#funcion area de un circulo
def area_circ(radio):
    import math
    area=math.pi*(radio**2);
    print(f"El area es {area} cm**2");
#funcion perimetro de un cuadrado
def perimetro_cuadrado(lado):
    perimetro=lado*4
    print(f"El perimetro del cuadrado es {perimetro}");
def menu():
    print("MEnu");
    print("1.-Calcular area de un circulo");
    print("2.-Calcular perimetro de un cuadrado");
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
    imc=peso/(estatura**2)
    if imc<18.5:
        print(f"Su imc es {imc} y usted se encuentra bajo peso")
    if 18.5<imc<24.9:
        print(f"Su imc es {imc} y usted se encuentra en peso normal")


def ejer1():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:
        print("MENOR DE EDAD")
    else:
        if edad >= 18 and edad <= 64:
            print("ADULTO")
        else:
            print("ADULTO MAYOR")

def ejer2():
     ano = int(input("Ingrese el año: "))
     
     if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
         print("El año es bisiesto")
     else:  
         print ("El año no es bisiesto")
     if ano %2 ==0:
        print("El año es par")
     else:
         print("El año no es par")

def ejer3():
    monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion=int(input("\nIngrese una opción: "))

    match opcion:
        case 1: print("Dolares: ",round((monto/3.75),0))
        case 2: print(f"Euros: {monto/4.05:.2f}")
        case _: print("Opción incorrecta...")
import math
def ejer4():
    print("Bienvenido al sistema de cálculos de áreas\n")
    print("1.Cuadrado")
    print("2.Rectangulo")
    print("3.Triangulo")
    print("4.Circulo\n")

    opcion = int(input("Ingrese una opción: "))
    
    match opcion: 
        case 1: 
            lado = int(input("ingrese un lado"))
            print("Área: ", lado*lado)
        case 2:
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Área: ", (bse*alt))
        case 3:
            bse2 = int(input("Ingrese la base: "))
            alt2 = int(input("Ingrese la altura: "))
            print("Área triángulo: ", (bse2*alt2)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("Área del circulo: ",(round(math.pi*radio**2),2))
        case _: print("Opción incorrecta")
ejer4()


    



def ejer1():
    nombre = input ("Ingrese su nombre: ")
    carrera = input ("Ingrese su carrera: ")
    print(f"{nombre}, bienvenido a FA de {carrera}")
def ejer2():
    print("\"Victor\"")
def ejer3():
  x=int(input("INgrese el valor de x: "))
  y=int(input("INgrese el valor de y: "))

  print("Suma: ",(x+y))
  print("Resta: ",(x-y))
  print("Multiplicación: ",(x*y))
  print("División: ",(x/y))
import math
def ejer4():
    num = float(input("Ingrese un numero decimal: "))
    print("Raiz 2: ", math.sqrt(num))
    print("Redondeado: ", round(num,0))
    print("Al cubo: ",math.pow(num,3))
    print("Raiz 3: ",num ** (1/3))
def ejer5():
    num = input("ingrese un número: ")

    entero = int(num)
    deci = float(num)

    print("Resto: ",(entero%2))
    print("División: ",(deci/3))


ejer5()
     
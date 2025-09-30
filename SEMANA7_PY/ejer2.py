import random

print("*************************************************")
print("*       Bienvenido al juego adivinador          *")
print("*                                               *")
print("* 1.Adivinar el numero entre 1 al 20            *")
print("* 2.Tienes 3 intentos                           *")
print("*************************************************")

intentos = 3
secreto = random.randint(1,20)

while intentos>0:
    num = int(input("\nIngrese el número: "))

    if secreto == num:
        print("\nCorrecto! Adivinaste el número. ")
        break
    else:
        intentos-=1
    if num < secreto: print("\nPista: El número es mayor", intentos)
    else: print("\npista. El número es menor. ", intentos)

else: print("\nno lograste adivinar el número ", secreto)

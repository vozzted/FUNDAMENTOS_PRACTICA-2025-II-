g = input("genere una contraseña: ")

print("\n------------------------------------")
print("--     Válida la contraseña       --")
print("--                                --")
print("°-    1. ud. tiene 3 intentos     -°")
print("------------------------------------\n")

intentos = 3

while( intentos > 0 ):
    c= input("Ingrese la contraseña: ")

    if g == c:
        print("\nAcceso concedido. Bienvenido al sistema Sr.Stark")
        break
    else:
        intentos-=1
        print("Contraseña incorrecta. Intentos restantes ", intentos)
         
else: print("Acceso denegado!!!!!!. Cerrando sistema. ")

while True: 
   num = int(input("Ingrese un numero positivo: "))
   suma = 0

   for i in range (1,num+1):
       suma += i
       print(i, end=" ")
      
   print("\nSuma: ",suma)    
   opc = input("¿Desea continuar?(S/N): ")

   if(opc =="N"): break



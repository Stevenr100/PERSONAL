print("PROGRAMA PARA ORDENAR DE FORMA DESCENDENTE TRES NÚMEROS")
print("")
num1= int (input("Ingrese el Primer Número: "))
num2= int (input("Ingrese el Segundo Número: "))
num3= int (input("Ingrese el Tercero Número: "))

if ((num1 <= num2)and (num1 <= num3)):
    menor = num1

    if(num2 <= num3):
        medio= num2
        mayor= num3

    else:
        medio= num3
        mayor= num2


elif ((num2 <= num1)and (num2 < num3)):
    menor= num2

    if(num1 <= num3):
        medio= num1
        mayor= num3

    else:
         medio= num3
         mayor= num1


else:
    menor = num3

    if (num1 <=num2):
          medio= num1
          mayor= num2

    else:
          medio= num2
          mayor= num1

print("")
print("EL ORDEN DESCENDENTE DE LOS NÚMEROS INGRESADOS ES: ")
print("")
print(str(mayor))
print(str(medio))
print(str(menor))

         

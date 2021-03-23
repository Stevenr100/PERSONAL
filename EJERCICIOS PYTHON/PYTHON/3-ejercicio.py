
print("PROGRAMA PARA SABER SI UN NÚMERO ES MAYOR, MENOR O IGUAL AL OTRO")
print("")
num1= float(input ("Ingrese el PRIMER Número: "))
num2= float(input ("Ingrese el SEGUNDO Número: "))

print("")
if num1 > num2:
    print("El NÚMERO",num2, " ES MENOR ")
    print("El NÚMERO",num1, " ES MAYOR")
elif num1 < num2:
    print("EL NÚMERO",num1, " ES MENOR ")
    print("EL NÚMERO",num2, " ES MAYOR")
else:
    print("LOS NÚMEROS SON IGUALES")

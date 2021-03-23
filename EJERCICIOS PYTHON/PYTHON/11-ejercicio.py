
print("PROGRAMA QUE PERMITE CALCULAR EL INDICE DE MASA CORPORAL")

print("")
num1= float(input ("Ingrese el Peso en kg: "))
num2= float(input ("Ingrese la Talla en m: "))

imc=num1/num2**2
print("")
if  imc < 20:
    
    print("SU ESTADO ES: DESNUTRIDO ")


elif  20 < imc < 25:

    print("SU ESTADO ES: NORMAL ")

    
elif 25 <= imc <= 30:

    print("SU ESTADO ES: SOBREPESO ")


elif  30 < imc < 35:

    print("SU ESTADO ES: OBESIDAD GRADO 1 ")


elif  35 <= imc <= 40:

    print("SU ESTADO ES: OBESIDAD GRADO 2 ")
    
elif num1 > 40:

    print("SU ESTADO ES: OBESIDAD GRADO 3 ")


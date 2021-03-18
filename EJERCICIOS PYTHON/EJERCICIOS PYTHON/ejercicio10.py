print ("PROGRAMA PARA DETERMINAR EL SALARIO A PAGAR A UN EMPLEADO")


num1= int (input("Ingrese el salario diario:  "))
num2= int (input("Ingrese el número de días trabajados:   "))


resul=num1*num2
porcentaje=resul*25/100

valorf=resul-porcentaje


print ("EL SALARIO QUE SE LE DEBE PAGAR AL EMPLEADO ES  ", valorf)



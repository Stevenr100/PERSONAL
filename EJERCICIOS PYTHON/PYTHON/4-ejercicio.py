
print("PROGRAMA PARA CALCULAR SI UN ESTUDIANTE APRUEBA O NO APRUEBA")
print("")
nota1= float(input ("Ingrese la Primer Nota de 0.0 a 5.0: "))
nota2= float(input ("Ingrese la Segunda Nota de 0.0 a 5.0: "))
nota3= float(input ("Ingrese la Tercera Nota de 0.0 a 5.0: "))
nota4= float(input ("Ingrese la Cuarta Nota de 0.0 a 5.0: "))
nota5= float(input ("Ingrese la Quinta Nota de 0.0 a 5.0: "))

promedio = (nota1+nota2+nota3+nota4+nota5)/5

print("")
if promedio >= 3.0:
    print("NOTA=",promedio,"  APROBO ")
    
elif promedio < 3.0:
    print("NOTA=",promedio,"  NO APROBO ")
    


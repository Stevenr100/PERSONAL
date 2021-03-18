print ("PROGRAMA PARA CONVERSIÓN DE UNIDADES DE TIEMPO")


horas= int (input("Escriba la cantidad de horas:  "))
minutos= int (input("Escriba la cantidad de minutos :  "))
segundos= int (input("Escriba la cantidad de segundos :  "))

segundos += horas * 60 * 60
segundos += minutos * 60




print ("LA CANTIDAD DE SEGUNDOS EN TOTAL ES: {} ".format(segundos))





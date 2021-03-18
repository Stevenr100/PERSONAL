print ("PROGRAMA PARA CONVERSIÓN DE UNUDADES DE LONGITUD")


num= int (input("Ingrese el valor de  la longitud en CM:  "))


milimetros=num*10
decimetros=num*0.1
decametros=num*0.001
hectometros=num*0.0001
kilometros=num/100000





print ("",num,"cm"," = ", milimetros, "mm")
print ("",num,"cm"," = ", decimetros, "dm")
print ("",num,"cm"," = ", decametros, "dam")
print ("",num,"cm"," = ", hectometros,"hm")
print ("",num,"cm"," = ", kilometros, "km")



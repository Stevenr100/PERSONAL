
cant=0
acomu=0

while(True):
    valor= float(input("nota: "))

    if (valor == 0):
        print("ERROR")
        break
    

    cant=cant + 1
    acomu=acomu + valor

print("")
promedio= acomu / cant
print("Promedio: " +str (promedio))


print("PROGRAMA QUE PERMITE CALCULAR EL NÚMERO DE PULSACIONES POR CADA 10 SEGUNDOS DE EJERCICIO AERÓBICO")

print("")
num1= float(input ("Ingrese su Edad: "))


print("")
def menu():

    print(" GENERO ")
    print("1. Masculino")
    print("2. Femenino")
   
    print("")
    op = input ("SELECCIONE SU GENERO: ")
    op = int(op)
    if op==1: primera()
    elif op==2: segunda()
    

    else: exit()
    print("")
    
def primera():
    print("")
    pul= (210-num1)/10
    print ("SUS PULSACIONES SON:  ", pul )
    print("")
    menu()
    
def segunda():
    print("")
    pul= (220-num1)/10
    print ("SUS PULSACIONES SON:  ", pul )
    print("")
    menu()
    

    
menu()





    

    
    



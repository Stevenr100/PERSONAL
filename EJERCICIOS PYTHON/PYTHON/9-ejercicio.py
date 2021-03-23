
print("PROGRAMA QUE PERMITE CALCULAR EL PRECIO A PAGAR EN UNA PIZZERIA")



print("")
def menu():

    print(" PIZZAS ")
    print("1. $15.000")
    print("2. $24.000")
    print("3. $36.000")

    op = input ("SELECCIONE QUE PIZZA QUIERE: ")
    op = int(op)
    if op==1: primera()
    elif op==2: segunda()
    elif op==3: tercera()

    else: exit()
    print("")
    
def primera():
    print("")
    print ("FACTURA PIZZAS ")
    print("")
    pizza= 15000
    num1 = int (input("Ingrese el Número de Ingredientes Adicionales: "))
    adicion=4000
    precio= pizza+(num1*adicion)
    print("")
    print ("El Valor a Pagar es: $ ", precio )
    print("")
    menu()
    
def segunda():
    print("")
    print ("FACTURA PIZZAS ")
    print("")
    pizza= 24000
    num1 = int (input("Ingrese el Número de Ingredientes Adicionales: "))
    adicion=4000
    precio= pizza+(num1*adicion)
    print("")
    print ("El Valor a Pagar es: $ ", precio )
    print("")
    menu()
    
def tercera():
    print("")
    print ("FACTURA PIZZAS ")
    print("")
    pizza= 36000
    num1 = int (input("Ingrese el Número de Ingredientes Adicionales: "))
    adicion=4000
    precio= pizza+(num1*adicion)
    print("")
    print ("El Valor a Pagar es: $ ", precio )
    print("")
    menu()
    
menu()





    

    
    


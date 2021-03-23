

num1 = float (input("Ingrese el Primer Número: "))
num2 = float(input("Ingrese el Segundo Número: "))


def menu():

    print("Menu de operaciones.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: suma()
    elif op==2: resta()
    elif op==3: multiplicacion()
    elif op==4: division()
    else: exit()
    
def suma():
    print("")
    print ("SUMA: ")
    print ("El Resultado es: ", num1+num2)
    print("")
    menu()
    
def resta():
    print("")
    print ("RESTA: ")
    print ("El Resultado es: ", num1-num2)
    print("")
    menu()
def multiplicacion():
    print("")
    print ("MULTIPLICACIÓN")
    print ("El Resultado es: ", num1*num2)
    print("")
    menu()
def division():
    print("")
    print ("DIVISIÓN")
    print ("El Resultado es: ", num1/num2)
    print("")
    menu()
    os.system ("cls") 
menu()



def menu():

    print("CALCULAR AREAS DE FIGURAS GEOMETRICAS.")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Circulo")
    print("5. Rombo")
    print("6. Trapecio")
    op = input ("Escriba la opción:")
    op = int(op)
    if op==1: cuadrado()
    elif op==2: rectangulo()
    elif op==3: triangulo()
    elif op==4: circulo()
    elif op==5: rombo()
    elif op==6: trapecio()
    else: exit()
    
def cuadrado():
    print("")
    print ("AREA DEL CUADRADO ")
    print("")
    num1 = float (input("Ingrese el Valor de un Lado del Cuadrado: "))
    print("")
    print ("El Area del Cuadrado es: ", num1**2)
    print("")
    menu()
    
def rectangulo():
    print("")
    print ("AREA DEL RECTÁNGULO ")
    print("")
    num1 = float (input("Ingrese la Base del Rectángulo: "))
    num2 = float (input("Ingrese la Altura del Rectángulo: "))
    print("")
    print ("El Area del Rectángulo es: ", num1*num2)
    print("")
    menu()
def triangulo():
    print("")
    print ("AREA DEL TRIÁNGULO ")
    print("")
    num1 = float (input("Ingrese la Base del Triángulo: "))
    num2 = float (input("Ingrese la Altura del Triángulo: "))
    print("")
    print ("El Area del Triángulo es: ", (num1*num2)/2)
    print("")
    menu()
def circulo():
    print("")
    print ("AREA DEL CIRCULO ")
    print("")
    num1 = float (input("Ingrese el Radio del Circulo: "))
    print ("El Area del Circulo es: ", 3.1416*num1**2 )
    print("")
    menu()
def rombo():
    print("")
    print ("AREA DEL ROMBO ")
    print("")
    num1 = float (input("Ingrese el Diagonal Mayor del Rombo: "))
    num2 = float (input("Ingrese el Diagonal Menor del Rombo: "))
    print ("El Area del Rombo es: ", (num1*num2)/2)
    print("")
    menu()
def trapecio():
    print("")
    print ("AREA DEL TRAPECIO ")
    print("")
    num1 = float (input("Ingrese la Base Mayor del Trapecio: "))
    num2 = float (input("Ingrese la Base Menor del Trapecio: "))
    num3 = float (input("Ingrese la Altura del Trapecio: "))
    print ("El Area del Trapecio es: ", (num1+num2)/2 *num3)
    print("")
    menu()
menu()



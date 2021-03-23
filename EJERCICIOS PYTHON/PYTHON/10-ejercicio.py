
print("PROGRAMA QUE PERMITE CALCULAR EL PRECIO PRODUCTOS")

print("")
num1= int(input ("Ingrese la cantidad de productos a comprados: "))
num2= int(input ("Ingrese el precio unitario original: "))


print("")
if  num1 <= 5:
    valor= num2*num1
    print("EL VALOR QUE DEBE PAGAR ES: $ ", valor)


elif  5 < num1 < 10:
    descuento=(num2*5)/100
    precio=num2-descuento
    valor= precio*num1
    print("EL VALOR QUE DEBE PAGAR ES: $ ", valor)

    
elif num1 >= 10:
    descuento=(num2*8)/100
    precio=num2-descuento
    valor= precio*num1
    print("EL VALOR QUE DEBE PAGAR ES: $ ", valor)


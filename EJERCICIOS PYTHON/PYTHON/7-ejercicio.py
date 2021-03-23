
print("PROGRAMA QUE PERMITE AL USUARIO TOMAR UNA DECISIÓN DEL TIPO DE PAGO A USAR")
print("")
cuenta= float(input ("Ingrese el valor que tiene en su Cuenta: "))


print("")
if  cuenta in range(300000,600000):
    print("PAGO CON TARJETA DE DÉBITO ")


elif cuenta < 150000:
    print(" PAGO EN EFECTIVO")

    
elif cuenta in range(150000,300000):
    print("PAGO CON EL CELULAR ")



else:
    print("PAGO CON LA TARJETA DE CREDITO")

    

    
    


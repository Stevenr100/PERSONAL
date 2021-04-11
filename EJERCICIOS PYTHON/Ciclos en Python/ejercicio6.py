
def binario_decimal(binario):
    posicion = 0
    decimal = 0
    
    binario = binario[::-1]
    for digito in binario:
        
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal


binario = input("Ingresa un número binario: ")
decimal = binario_decimal(binario)
print("el número covertido a decimal es: ", decimal)

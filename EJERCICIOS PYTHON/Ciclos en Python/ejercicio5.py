
precios = [80000, 75000, 98000, 22500, 84000, 65000, 12000, 58000,6400]

min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print("El menor precio es " + str(min)) 
print("El mayor precio es " + str(max))


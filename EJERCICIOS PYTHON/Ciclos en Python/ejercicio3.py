import random

lanzamiento= input("Desea Lanzar los dados s/n: ")
while (lanzamiento =='s'):
        
    dado = random.randint(1,6)
    print("El dado cayo en: " + str(dado))

    if dado == 3:
        print("")
        print("FIN, EL DADO CAYO EN EL NÚMERO 3")
        break


if lanzamiento == 'n':
    print("")
    print("BYE...")


if lanzamiento != 's':
    print("")
    print("NO SELEECIONASTE LAS LETRAS CORRECTAS...")




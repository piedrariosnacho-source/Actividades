numero = int(input("Escribe un número: "))
divi = 2
primo = True

if numero <= 1:
    print("numero no aceptado")

    if numero % divi == 0:
        primo = False
    else:
        divi += 1

    if primo == True:
        print("Es primo")
    else:
        print("No es primo")
edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Error: la edad no puede ser negativa.")

else:
    dia = input("Introduce el día de la semana: ")
    tres_d = input("¿La sesión es 3D? (si/no): ")

    if edad < 12:
        precio = 5
    elif edad < 65:
        precio = 8
    else:
        precio = 6

    print("Precio base:", precio, "€")

    match dia:
        case "miércoles":
            precio = precio - 1
            print("Descuento miércoles: -1 €")
        case _:
            print("Descuento miércoles: 0 €")

    match tres_d:
        case "si":
            precio = precio + 2
            print("Sesión 3D: +2 €")
        case "no":
            print("Sesión 3D: 0 €")

    print("Precio final:", precio, "€")

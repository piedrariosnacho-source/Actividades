sala = 0
accion = ""

while accion != 3:
    print("1) Entra")
    print("2) Sale")
    print("3) Fin")
    accion = input("Elige una opción: ")

if accion == 1 and sala <= 8:
    sala = sala + 1
elif accion == 1 and sala > 8:
    print("No existen plazas libres")

if accion == 2 and sala >= 1:
    sala = sala - 1
elif accion == 2 and sala < 1:
    print("la sala ya está vacía")

if accion == 3:
    print("se han quedado", sala)

if accion >= 3:
    print(accion)
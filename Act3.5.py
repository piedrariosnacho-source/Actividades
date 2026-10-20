import random

titular = True
saldo = random.randint(0, 1000)
cuenta = True
estado = ""

if cuenta == True:
    estado = "activa"
elif cuenta == False:
    estado = "cerrada"

while accion != 6:
    print("1) Ingresar")
    print("2) retirar")
    print("3) consultar")
    print("4) cerrar cuenta")
    print("5) abrir cuenta")
    print("6) salir")
    accion = input("Elige una opción: ")

if accion == 1 and cuenta == True:
    saldo = saldo + int(input("cantidad a ingresar: "))

if accion == 2 and cuenta == True and saldo > 0:
    saldo = saldo - int(input("cantidad a ingresar: "))

if accion == 3:
    print(titular, saldo, estado)

if accion == 4 and cuenta == True and saldo == 0:
    cuenta = False
    print("cuenta cerrada")

if accion == 5 and cuenta == False:
    cuenta = True
    saldo = 0
    print("cuenta abierta")

if accion == 6:
    print("Estado final de la cuenta:")
    print("Titular:", titular)
    print("Saldo:", saldo)
    print("Estado:", estado)
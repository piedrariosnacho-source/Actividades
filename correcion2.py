import random
operacion = input("qué opreción quieres realizar: ingresar, retirar, abrir cuenta, cerrar cuenta o consultar")
operacion_simple = operacion.lower().strip()
saldo = random.randint(0,1000)
titular = Mario
Estado = true

match comando:
    case "ingresar":
        cantidad = int(input("dinero a ingresar: "))
        if cantidad > 0:
            saldo +=  cantidad
        else:
            print("cantidad no válida")
    case "retirar":
        cantidad = int(input("dinero a retirar: "))
        if cantidad > 0 and saldo >= cantidad:
            saldo -= cantidad
        else:
            print("cantidad no válida")
    case "abrir":
        if not Estado:
             Estado = True
    case "cerrar":
        if Estado and saldo >= 0:
            Estado = False
    case "consultar":
            print("operación no válida")
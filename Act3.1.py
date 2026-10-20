Codigo = "4826"
Error = "Código Incorrecto"
Escribe = input("Escribe el codigo: ")
contador = int(3)


while Escribe != Codigo:
    contador = contador - 1
    print("Error")
    Escribe = input("Escribe el codigo: ")
    if contador == 0:
        print("Máximo de intentos alcanzado")
        break

    elif Escribe == Codigo:
        print("Acceso autorizado")
        break
        
    

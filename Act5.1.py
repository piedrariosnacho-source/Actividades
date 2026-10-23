TIEMPO_CINE = 2
DINERO_CINE = 10
TIEMPO_COMER = 2
DINERO_COMER = 30
TIEMPO_MUSEO = 1
DINERO_MUSEO = 5
TIEMPO_DEPORTE = 1
DINERO_DEPORTE = 0
TIEMPO_CASA = 3
DINERO_CASA = 0

dinero = int(input("Cuánto dinero te quieres gastar como máximo?"))
tiempo = int(input("Cuánto tiempo tienes?"))
actividades= ""


def mostrar_opciones():
    print("1. Ir al cine (10€ / 2 horas)")
    print("2. Ir a comer (30€ / 2 horas)")
    print("3. Visitar un museo (5€ / 1 horas)")
    print("4. Hacer deporte (0€ / 1 horas)")
    print("5. Quedarse en casa (0€ / 3 horas)")

def main():
    while dinero > 0 and tiempo > 0:
        mostrar_opciones()
        opcion = int(input("¿Qué quieres hacer?: "))

        match opcion:
            case 1:
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE
                actividades += "Ir al cine (10€ / 2 horas)"
            
            case 2:
                dinero -= DINERO_COMER
                tiempo -= TIEMPO_COMER
                actividades += " Ir a comer (30€ / 2 horas)"
            
            case 3:
                dinero -= DINERO_MUSEO
                tiempo -= TIEMPO_MUSEO
                actividades += "Visitar un museo (5€ / 1 horas)"
            
            case 4:
                dinero -= DINERO_DEPORTE
                tiempo -= TIEMPO_DEPORTE
                actividades += "Hacer deporte (0€ / 1 horas)"
           
            case 5:
                dinero -= DINERO_CASA
                tiempo -= TIEMPO_CASA
                actividades += "Quedarse en casa (0€ / 3 horas)"

            case _:
                print("Opción no válida")

    
    print(actividades)
            

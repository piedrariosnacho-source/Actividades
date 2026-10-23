palabra = input("Ingrese una palabra: ")
letras = {}

for letra in palabra:
    if not letra in letras:
        letras[letra] = palabra.count(letra)

print(list(letras))


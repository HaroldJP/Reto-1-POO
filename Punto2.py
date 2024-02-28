def palindromo():
    palabra = input("Ingrese su palabra en minúsculas para verificar si es un palíndromo: ")
    palabra_invertida = ""

    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    if palabra == palabra_invertida:
        print(f"La palabra {palabra} es un palíndromo.")
    else: print(f"La palabra {palabra} no es un palíndromo.")

if __name__== "__main__":
    palindromo()

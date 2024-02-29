def tienen_mismos_caracteres(palabra1, palabra2):
    # Ordenamos los caracteres de ambas palabras y los comparamos
    return sorted(palabra1) == sorted(palabra2)

def palabras_con_mismos_caracteres(lista):
    resultado = []
    for i in range(len(lista)):
        palabra_actual = lista[i]
        misma_palabra = False
        for j in range(i + 1, len(lista)):
            if tienen_mismos_caracteres(palabra_actual, lista[j]):
                misma_palabra = True
                break
        if misma_palabra:
            resultado.append(palabra_actual)
    return resultado

def main():
    entrada = input("Ingrese la lista de palabras separadas por comas: ")
    lista = entrada.split(",")
    palabras_con_mismos = palabras_con_mismos_caracteres(lista)
    print("Palabras con los mismos caracteres:", palabras_con_mismos)

if __name__ == "__main__":
    main()

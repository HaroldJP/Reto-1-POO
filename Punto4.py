def mayor_suma_consecutiva(lista):
    if len(lista) < 2:
        return "La lista debe contener al menos dos elementos para calcular la suma consecutiva."
    
    max_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > max_suma:
            max_suma = suma_actual
    
    return max_suma

def numeros():
    lista = []
    a = int(input("Ingrese cuántos números quiere agregar: "))
    b = 1
    while b <= a:
        c = int(input("Ingrese un número entero: "))
        lista.append(c)
        b += 1
    return lista

if __name__ == "__main__":
    lista_numeros = numeros()
    print("Lista de números:", lista_numeros)
    resultado = mayor_suma_consecutiva(lista_numeros)
    print("La mayor suma entre dos elementos consecutivos es:", resultado)

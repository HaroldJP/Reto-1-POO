# Reto-1-POO
## Punto 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```python
def operaciones():    
    operacion = input("Ingrese qué tipo de operación quiere hacer con alguno de los siguientes símbolos (+, -, *, /): ")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    if operacion == "+":
        c = a + b
        print(f"La suma entre los números {a} y {b} es {c}")
    elif operacion == "-":
        c = a - b
        print(f"La diferencia entre {a} y {b} es {c}")    
    elif operacion == "*":
        c = a * b
        print(f"El producto entre {a} y {b} es {c}")
    elif operacion == "/":
        c = a / b
        print(f"La división entre {a} y {b} es {c}")


if __name__ == "__main__":
    operaciones()
```

## Punto 2

Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python
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
```

##Punto 3

Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```python
lista = []

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros():
    a = int(input("Ingrese cuántos números quiere agregar: "))
    b = 1
    while b <= a:
        c = int(input("Ingrese un número: "))
        lista.append(c)
        b += 1
    return lista

if __name__ == "__main__": 
    numeros()
    print("Lista completa:", lista)
    
    primos = [numero for numero in lista if es_primo(numero)]
    print("Números primos en la lista:", primos)
```

## Punto 4

Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.


```python
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
```

## Punto 5



```python
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
```




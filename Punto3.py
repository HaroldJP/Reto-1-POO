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

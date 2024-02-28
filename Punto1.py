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

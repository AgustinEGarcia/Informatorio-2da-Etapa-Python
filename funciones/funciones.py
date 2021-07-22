def saludar():
    print("Hola")


# saludar()


# Si una función no tiene return, por defecto devuelve none, el valor null de Python

def suma(a, b):
    return a + b


# print(suma(2, 5))

def sumas(*args):
    for item in args:
        print(item)


# sumas(1, 2, 4, 5, 6)

def sumar(*args):
    total = 0
    for num in args:
        total = total + num
    return  total


print(sumar(1, 2, 4, 5, 6))

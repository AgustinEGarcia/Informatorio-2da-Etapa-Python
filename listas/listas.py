"""
def ingresoDatos():
    lista_numeros = []
    for i in range(0, 5):
        num = input(f"Ingrese el número {i} --> ")
        lista_numeros.append(num)
    print("Los datos ingresados son: ")
    print(lista_numeros)

ingresoDatos()

"""


def puntoA():
    num = 1

    lista_numeros = []

    while num != 0:
        num = int(input("Ingrese un número, si envía 0, el ingreso de números finaliza: "))

        if num != 0:
            lista_numeros.append(num)

    print("Los números ingresados son: ")
    print(lista_numeros)

    return lista_numeros


def puntoB(lista_numeros):
    num = 0

    num = int(input("Ingrese un número para eliminar: "))

    for elem in lista_numeros:

        if elem == num:
            lista_numeros.remove(elem)

            print("Lista modificada: ")

            print(lista_numeros)

            return

    print("El número ingresado no se encuentra en la lista")

    return lista_numeros


def puntoC(lista_numeros):
    sumatoria = 0

    for num in lista_numeros:
        sumatoria += num

    print(f"La sumatoria de los números de la lista es {sumatoria}")


def puntoD(lista_numeros):
    lista_menores = []

    num = int(input("Ingrese un número para comparar: "))

    for elem in lista_numeros:

        if elem < num:
            lista_menores.append(elem)

    print(f"La nueva lista con números menores que {num} es: ")
    print(lista_menores)


def yaRecorrido(lista_numeros, num):
    for item in lista_numeros:
        if item == num:
            return True

    return False


def puntoE(lista_numeros):
    cont = 0
    lista_ya_recorridos = list()
    lista_tuplas = list()

    for item in lista_numeros:

        if not yaRecorrido(lista_ya_recorridos, item):

            lista_ya_recorridos.append(item)

            for item2 in lista_numeros:

                if item == item2:
                    cont += 1

            lista_tuplas.append((item, cont))
            cont = 0

    print("Lista de repeticiones generadas: ")
    print(lista_tuplas)

puntoE(puntoA())



diccionario_maestro = {}

def agregarCliente(diccionario):

    dni = int(input("Ingrese el DNI -> "))

    nombre = input("Ingrese el nombre -> ")
    apellido = input("Ingrese el apellido -> ")
    mail = input("Ingese el mail -> ")

    diccionario[dni] = {nombre, apellido, mail}

    return diccionario

def eliminarCliente(diccionario):

    dni = int(input("Ingrese el DNI -> "))

    try:
        del diccionario[dni]
        print(diccionario)
    except KeyError:
        print("El cliente que desea eliminar no se encuentra en la Base de Datos.")

def getCliente(diccionario):

    dni = int(input("Ingrese el DNI -> "))

    try:
        print(diccionario[dni])
    except KeyError:
        print("El cliente solicitado no se encuentra en la Base de Datos.")

def terminar(diccionario):

    diccionario.clear()

    return diccionario

print("-----------------Base de Datos-------------------------")

flag = 1

while flag == 1:

    print("1) Añadir cliente.")
    print("2) Eliminar cliente.")
    print("3) Mostrar cliente.")
    print("4) Terminar.")

    opcion = int(input("Seleccione una opción --> "))

    if opcion == 1:

        print(agregarCliente(diccionario_maestro))

    elif opcion == 2:

        eliminarCliente(diccionario_maestro)

    elif opcion == 3:

        getCliente(diccionario_maestro)

    elif opcion == 4:

        print(terminar(diccionario_maestro))

    flag = int(input("Si desea continuar presione 1, de lo contrario 0 --> "))

if flag == 0:

    print(terminar(diccionario_maestro))
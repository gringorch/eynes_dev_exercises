'''
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
'''
import random as rd


def lista_dict():
    lista = []

    for i in range(10):
        edad = rd.randint(1, 100)
        dict = {}
        dict = {'ID': i+1, 'Edad': edad}
        lista.append(dict)

    return lista


def ordenar_lista(lista):

    orden = sorted(lista, key=lambda a: a['Edad'], reverse=True)

    print(
        f'El ID de la persona mas joven es el ID: {orden[-1]["ID"]}, Edad: {orden[-1]["Edad"]}')
    print(
        f'El ID de la persona mas vieja es el ID: {orden[0]["ID"]}, Edad: {orden[0]["Edad"]}')

    return orden

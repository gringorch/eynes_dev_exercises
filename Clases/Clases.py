'''
Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
'''
import numpy as np


class Circulo:

    def __init__(self, radio=1):
        if radio > 0:
            self.radio = radio
        else:
            print(
                "La instanciación no fue creada por un valor de radio incorrecto")
            Circulo()

    def __del__(self):
        print("instanciación no realizada")

    def modificar_radio(self, radio):
        if radio > 0:
            self.radio = radio
        else:
            print(
                "No se pudo realizar la modificación por ser un valor de radio incorrecto")

    def area(self):
        area = np.pi*self.radio**2
        return area

    def perimetro(self):
        perimetro = 2 * np.pi * self.radio
        return perimetro

    def __str__(self):
        return f"El circulo tiene un radio de {self.radio}"

    def __mul__(self, other):
        if other > 0:
            return Circulo(self.radio * other)
        else:
            print("La instanciación no fue creada por un valor de radio incorrecto")

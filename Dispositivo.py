import tkinter as tk

class dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self._seleccion = 0
        self._potencia = 0  # Atributos privados con un guion bajo al principio
        self._voltaje = 0
        self._corriente = 0
        self._tiempo = 0

    # Getter para verificar seleccion
    def get_name(self):
        return self.nombre

    # Getter para verificar seleccion
    def get_seleccion(self):
        return self._seleccion

    # Setter para verificar seleccion
    def set_seleccion(self, seleccion):
        if seleccion >= 0:
            self._seleccion = seleccion
        else:
            print("La potencia no puede ser un valor negativo.")

    # Getter para obtener la potencia
    def get_potencia(self):
        return self._potencia

    # Setter para configurar la potencia
    def set_potencia(self, potencia):
        if potencia >= 0:
            self._potencia = potencia
        else:
            print("La potencia no puede ser un valor negativo.")

    # Getter para obtener el voltaje
    def get_voltaje(self):
        return self._voltaje

    # Setter para configurar el voltaje
    def set_voltaje(self, voltaje):
        if voltaje >= 0:
            self._voltaje = voltaje
        else:
            print("El voltaje no puede ser un valor negativo.")

    # Getter para obtener la corriente
    def get_corriente(self):
        return self._corriente

    # Setter para configurar la corriente
    def set_corriente(self, corriente):
        if corriente >= 0:
            self._corriente = corriente
        else:
            print("La corriente no puede ser un valor negativo.")

    # Getter para obtener el tiempo
    def get_tiempo(self):
        return self._tiempo

    # Setter para configurar el tiempo
    def set_tiempo(self, tiempo):
        if tiempo >= 0:
            self._tiempo = tiempo
        else:
            print("El tiempo no puede ser un valor negativo.")

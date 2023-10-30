'''
Universidad del Valle de Guatemala
Parcial 3 - Física 3
Energía eléctica
 ---> Cálculo de costo y calibre

Fabiola Contreras 22787
María José Villafuerte 22129
'''

# Importamos las librerías necesarias para la simulación.
from tkinter import DoubleVar
import numpy as np # Libreria científica y matemática para Python.

def Confirmacion_potencia(voltaje_Total, Corriente):
    potencia_total = voltaje_Total*Corriente
    return potencia_total

def calculo_costo(kilowats, horas, dias):
    total_pago= kilowats*horas*dias*(0.13602)
    return total_pago

def calculo_calibre(Corriente_Total, largo_Cable, voltaje_total):
    #V = IR --> R = pL/(pi/4)*d^2 --> V = IpL/(pi/4)*d^2
    #d^2 = IpL/V*(pi/4)
    
    resistividad = 1.72*10**(-8)
    numerador = Corriente_Total*resistividad*largo_Cable.get()
    denominador = voltaje_total*(np.pi/4)
    if denominador !=0:
        diametro = np.sqrt(numerador/denominador)
    else:
        diametro = 0

    if 0 < diametro <= 0.163:
        return 14
    elif 18 < diametro <= 0.205:
        return 12

    elif 25 < diametro <= 0.259:
        return 10

    elif 30 < diametro <= 0.326:
        return 8

    elif 40 < diametro <= 0.412:
        return 6

    elif 60 < diametro <= 0.462:
        return 5

    elif 65 < diametro <= 0.519:
        return 4

    else:
        return 0
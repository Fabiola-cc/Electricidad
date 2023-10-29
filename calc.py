'''
Universidad del Valle de Guatemala
Parcial 3 - Física 3
Energía eléctica
 ---> Cálculo de costo y calibre

Fabiola Contreras 22787
María José Villafuerte 22129
'''
#LIBRERIAS PARCIAL 1, DEJAR LAS NECESARIAS :)
# Importamos las librerías necesarias para la simulación.
from tkinter import DoubleVar
import numpy as np # Libreria científica y matemática para Python.
from scipy import constants, integrate   # Librerias para integrar funciones en un intervalo dado.
'''
Diccionario: 


'''

def Confirmacion_potencia(voltaje_Total, Corriente_Total):
    potencia_total = voltaje_Total*Corriente_Total
    return potencia_total

def calculo_costo(kilowats, horas,dias):
    total_pago= kilowats*horas*dias*(0.13602)
    return total_pago

def calculo_calibre(Corriente_Total):
    calibre = 0
    diamentro = 0
    if 0 < Corriente_Total <= 18:
        calibre = 14
        diamentro=0.163
    elif 18 < Corriente_Total <= 25:
        calibre = 12
        diamentro=0.205

    elif 25 < Corriente_Total <= 30:
        calibre = 10
        diamentro=0.259

    elif 30 < Corriente_Total <= 40:
        calibre = 8
        diamentro=0.326

    elif 40 < Corriente_Total <= 60:
        calibre = 6
        diamentro=0.412

    elif 60 < Corriente_Total <= 65:
        calibre = 5
        diamentro=0.462

    elif 65 < Corriente_Total <= 85:
        calibre = 4
        diamentro=0.519

    elif Corriente_Total > 85:
        "La corriente es mayor al que este programa calcula, prueba con otro tipo de corriente"

    else:
        print("La corriente total es menor o igual a 0.")
    
    return calibre,diamentro
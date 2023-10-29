'''
Universidad del Valle de Guatemala
Parcial 3 - Física 3
Energía eléctica
 ---> Graficación de circuito

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np


def mostrar_grafica(dispositivos=[]):
    # Definir los puntos en el tiempo
    images = []

    for i,yeare in enumerate(dispositivos):
        images.append("imagen1.png")

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dispositivos, [0] * len(dispositivos), marker='', linestyle='-', color='b')  # Línea recta en el eje x
    #ax.plot(dispositivos, [0.1] * len(dispositivos), marker='o', linestyle='-', color='b')  # Línea recta en el eje x
    plt.ylim(-1, 1) 
    plt.xlim(-1, dispositivos.size()) 

    # Agregar las imágenes en los puntos deseados
    for i, image_file in enumerate(images):
        if i % 2 == 0:
            y_points = [0, 0.3]
            cambio = 0.6
            nombre = 0.34
        else:
            y_points = [0, -0.3]
            cambio = -0.6
            nombre = -0.38
        x_points = [i, i]
        plt.plot(x_points, y_points, marker = 'o', linestyle='-', color='b')
        img = plt.imread(image_file)
        imagebox = OffsetImage(img, zoom=0.05)
        ab = AnnotationBbox(imagebox, (dispositivos[i], cambio), frameon=False)
        ax.add_artist(ab)
        ax.text(dispositivos[i], nombre, dispositivos[i], ha='center')  

    # Añadir etiquetas y título
    plt.title('Dispositivos')
    plt.yticks([])  # Ocultar el eje y
    plt.xticks([])
    # Mostrar el gráfico
    plt.show()





    



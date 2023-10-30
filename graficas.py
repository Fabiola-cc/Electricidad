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


def mostrar_grafica(nombres, dispositivos, texto_calibre, texto_cobro, tipo_factura):
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(nombres, [0] * len(dispositivos), marker='', linestyle='-', color='b')  # Línea recta en el eje x
    #ax.plot(dispositivos, [0.1] * len(dispositivos), marker='o', linestyle='-', color='b')  # Línea recta en el eje x
    plt.ylim(-1, 1) 
    plt.xlim(-1, len(dispositivos)) 

    # Agregar las imágenes en los puntos deseados
    for i, disp in enumerate(dispositivos):
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
        img = plt.imread(disp.imagen)
        imagebox = OffsetImage(img, zoom=0.05)
        ab = AnnotationBbox(imagebox, (disp.nombre, cambio), frameon=False)
        ax.add_artist(ab)
        ax.text(disp.nombre, nombre, disp.nombre, ha='center')  

    # Añadir etiquetas y título
    plt.title('Dispositivos')

    # Agregar texto en coordenadas específicas
    plt.text(-1, -1.08, texto_calibre, fontsize=10)
    plt.text(-1, -1.15, texto_cobro, fontsize=10)
    plt.text(-1, -1.22, tipo_factura, fontsize=10)

    plt.yticks([])  # Ocultar el eje y
    plt.xticks([])
    # Mostrar el gráfico
    plt.show()

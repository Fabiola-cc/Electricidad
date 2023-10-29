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
import plotly.express as px


'''
Esto tenes que escribir en el main 

        nombres = [dispositivo.get_name() for dispositivo in datos]
        graficas.mostrar_circuito(nombres)


'''



# Definir los puntos en el tiempo
years = ["Televisor", "Televisor_1", "Televisor_2", "Televisor_3", "Televisor_4", "Televisor_5","Televisor_6","Televisor_7"]
images = []

for i,yeare in enumerate(years):
    images.append("imagen1.png")

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 2.2))
ax.plot(years, [0] * len(years), marker='o', linestyle='-', color='b')  # Línea recta en el eje x

# Agregar las imágenes en los puntos deseados
for i, image_file in enumerate(images):
    img = plt.imread(image_file)
    imagebox = OffsetImage(img, zoom=0.2)
    ab = AnnotationBbox(imagebox, (years[i], 0.5), frameon=False)
    ax.add_artist(ab)

# Añadir etiquetas y título
plt.title('Dispositivos')
plt.yticks([])  # Ocultar el eje y

# Mostrar el gráfico
plt.show()



    



'''
Universidad del Valle de Guatemala
Parcial 3 - Física 3
Energía eléctica
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import tkinter as tk # Libreria para creacion de interfaz grafica
from tkinter import ttk

#Documentos de otras clases
from Dispositivo import dispositivo
import calc
import graficas

#Creacion de pantalla
ventana = tk.Tk()
ventana.geometry("700x650")

def clear_frame():
    for widgets in ventana.winfo_children():
      widgets.destroy()

#Opciones
elementos = [
    dispositivo("Televisión"),
    dispositivo("Computadora"),
    dispositivo("Teléfono"),
    dispositivo("Consola de Juegos"),
    dispositivo("Router WiFi"),
    dispositivo("Impresora"),
    dispositivo("Refrigeradora"),
    dispositivo("Microondas"),
    dispositivo("Cafetera"),
    dispositivo("Tostadora"),
    dispositivo("Air Fryer"),
    dispositivo("Licuadora"),
    dispositivo("Batidora"),
    dispositivo("Lavadora"),
    dispositivo("Secadora"),
    dispositivo("Plancha de Ropa"),
    dispositivo("Aspiradora"),
    dispositivo("Ventilador"),
    dispositivo("Luces"),
    dispositivo("Cámara de Seguridad")]

def crear_contenido(frame):
    fila_actual = 6  # Fila inicial

    # Listas para almacenar las variables de entrada
    seleccionados = []
    variables_potencia = []
    variables_voltaje = []
    variables_corriente = []
    variables_tiempo = []

    for i, dispositivo in enumerate(elementos):
        if i % 2 == 0:
            columna = 0
            fila_actual += 6
        elif i == 1:
            columna = 5
        else:
            columna = 5

        Input_Seleccion = tk.IntVar()
        seleccionados.append(Input_Seleccion)
        tk.Checkbutton(frame, text=dispositivo.nombre, variable=Input_Seleccion).grid(row=fila_actual, column=columna, sticky="w")

        # Crear variables para potencia, voltaje, corriente y tiempo
        variable_potencia = tk.DoubleVar()
        variable_voltaje = tk.DoubleVar()
        variable_corriente = tk.DoubleVar()
        variable_tiempo = tk.DoubleVar()

        # Agregar las variables a las listas
        variables_potencia.append(variable_potencia)
        variables_voltaje.append(variable_voltaje)
        variables_corriente.append(variable_corriente)
        variables_tiempo.append(variable_tiempo)

        # Etiquetas y campos de entrada para potencia, voltaje, corriente y tiempo
        ttk.Label(frame, text="Potencia (W):", font="Times 8").grid(row=fila_actual + 1, column=columna, sticky="w")
        ttk.Entry(frame, textvariable=variable_potencia, width=5).grid(row=fila_actual + 1, column=columna + 1)

        ttk.Label(frame, text="Voltaje (V):", font="Times 8").grid(row=fila_actual + 2, column=columna, sticky="w")
        ttk.Entry(frame, textvariable=variable_voltaje, width=5).grid(row=fila_actual + 2, column=columna + 1)

        ttk.Label(frame, text="Corriente (A):", font="Times 8").grid(row=fila_actual + 3, column=columna, sticky="w")
        ttk.Entry(frame, textvariable=variable_corriente, width=5).grid(row=fila_actual + 3, column=columna + 1)

        ttk.Label(frame, text="Tiempo (h):", font="Times 8").grid(row=fila_actual + 4, column=columna, sticky="w")
        ttk.Entry(frame, textvariable=variable_tiempo, width=5).grid(row=fila_actual + 4, column=columna + 1)

        ttk.Label(frame, text="", font="Times 8").grid(row=fila_actual + 5, column=columna, sticky="w")
    ttk.Label(frame, text="", font="Times 8").grid(row=fila_actual +6, column=0, columnspan=10)
    ttk.Button(frame, text="Listo", command=lambda: recopilar_informacion(seleccionados, variables_potencia, variables_voltaje, variables_corriente, variables_tiempo)).grid(row=fila_actual + 7, column=0, columnspan=10)

def recopilar_informacion(seleccionados, variables_potencia, variables_voltaje, variables_corriente, variables_tiempo):
    datos = []
    for i, dispositivo in enumerate(elementos):
            dispositivo.set_seleccion(seleccionados[i].get())
            dispositivo.set_potencia(variables_potencia[i].get())
            dispositivo.set_voltaje(variables_voltaje[i].get())
            dispositivo.set_corriente(variables_corriente[i].get())
            dispositivo.set_tiempo(variables_tiempo[i].get())

    for dispositivo in elementos:
        if dispositivo.get_seleccion() == 1:
            datos.append(dispositivo)

    if len(datos) <= 10 and len(datos) != 0:
        pass #HACER CALCULOS
    else:
        main()

def main():
    clear_frame()
    # Crear un Scrollbar vertical
    scrollbar = tk.Scrollbar(ventana, orient="vertical")

    # Crear un Canvas para contener el contenido deslizable
    canvas = tk.Canvas(ventana, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    # Asociar el Scrollbar con el Canvas
    scrollbar.config(command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="n") 

    # Configurar el Scrollbar para ajustar al contenido
    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    # Encabezado
    ttk.Label(frame, text="\nEjercicio 5 - Parcial 3 - Física 3", font="Times 10 italic").grid(row=0, column=0, columnspan=15)
    ttk.Label(frame, text="Fabiola Contreras 22787\tMaría José Villafuerte 22129", font="Times 10 italic").grid(row=1, column=0, columnspan=10)
    
    # Título
    ttk.Label(frame, text="¿Qué elementos deseas tomar en consideración?", font="Times 20").grid(row=2, column=0, columnspan=10)
    ttk.Label(frame, text="Para cada uno de los elementos que selecciones ingresa su potencia, voltaje, corriente y las horas de uso diarias del mismo", font="Times 8").grid(row=3, column=0, columnspan=10)
    ttk.Label(frame, text="Selecciona como máximo 10 dispositivos para la simulación, de lo contrario no se completará el proceso", font="Times 8").grid(row=4, column=0, columnspan=10)
    ttk.Label(frame, text="", font="Times 8").grid(row=5, column=0, columnspan=10)

    # Llamar a la función para crear contenido
    crear_contenido(frame)
    ventana.mainloop()

if __name__ == "__main__":
    main()
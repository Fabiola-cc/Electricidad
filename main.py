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
ventana.geometry("800x650")

def clear_frame():
    for widgets in ventana.winfo_children():
      widgets.destroy()
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

    return frame

#Opciones
elementos = [
    dispositivo("Televisión", imagen= "imagenes/tv.jpg"),
    dispositivo("Computadora", imagen= "imagenes/pc.jpg"),
    dispositivo("Teléfono", imagen= "imagenes/telefono.jpg"),
    dispositivo("Consola de Juegos", imagen= "imagenes/videojuego.jpg"),
    dispositivo("Router WiFi", imagen= "imagenes/wifi.jpg"),
    dispositivo("Impresora", imagen= "imagenes/impresora.jpg"),
    dispositivo("Refrigeradora", imagen= "imagenes/refri.jpg"),
    dispositivo("Microondas", imagen= "imagenes/microondas.png"),
    dispositivo("Cafetera", imagen= "imagenes/cafe.jpg"),
    dispositivo("Tostadora", imagen= "imagenes/tostadora.png"),
    dispositivo("Air Fryer", imagen= "imagenes/airfryer.jpg"),
    dispositivo("Licuadora", imagen= "imagenes/licuadora.jpg"),
    dispositivo("Batidora", imagen= "imagenes/batidora.jpg"),
    dispositivo("Lavadora", imagen= "imagenes/lavadora.png"),
    dispositivo("Secadora", imagen= "imagenes/secadora.jpg"),
    dispositivo("Plancha de Ropa", imagen= "imagenes/plancha.jpg"),
    dispositivo("Aspiradora", imagen= "imagenes/aspiradora.jpg"),
    dispositivo("Ventilador", imagen= "imagenes/ventilador.jpg"),
    dispositivo("Luces", imagen= "imagenes/luz.jpg"),
    dispositivo("Cámara de Seguridad", imagen= "imagenes/camara.jpg")]

def seleccion_dispositivos(frame):
    # Listas para almacenar las variables de entrada
    seleccionados = []
    for i, dispositivo in enumerate(elementos):
        fila = i // 2 + 5  # Ajustar las filas para etiquetas y campos de entrada
        columna = i % 2 * 5  # Alternar entre dos columnas para casillas de verificación

        Input_Seleccion = tk.IntVar()
        seleccionados.append(Input_Seleccion)
        tk.Checkbutton(frame, text=dispositivo.nombre, variable=Input_Seleccion).grid(row=fila, column=columna, sticky="w")

    ttk.Label(frame, text="", font="Times 8").grid(row=fila + 1, column=0, columnspan=10)
    ttk.Button(frame, text="Listo", command=lambda: agregar_datos(seleccionados)).grid(row=fila + 2, column=0, columnspan=10)

def agregar_datos(seleccionados):
    frame = clear_frame()
    #Solicitud largo
    ttk.Label(frame, text="", font="Times 10").grid(row=1, column=0, columnspan=10)
    ttk.Label(frame, text="¿cual es el largo del cable que conectará a los dispositivos?", font="Times 12").grid(row=2, column=0, columnspan=3)
    largo_cable = tk.DoubleVar()
    ttk.Entry(frame, textvariable=largo_cable, width=15).grid(row=3, column=0, columnspan=3)

    #Datos dispositivos
    ttk.Label(frame, text="Para cada uno de los elementos que selecciones ingresa su potencia, voltaje, corriente y las horas de uso diarias del mismo", font="Times 12").grid(row=4, column=0, columnspan=10)
    ttk.Label(frame, text="", font="Times 10").grid(row=5, column=0, columnspan=10)
    fila_actual = 6  # Fila inicial

    # Listas para almacenar las variables de entrada
    dispositivos=[]
    variables_potencia = []
    variables_voltaje = []
    variables_corriente = []
    variables_tiempo = []

    for i, valor in enumerate(seleccionados):
        if valor.get() == 1:
            dispositivos.append(elementos[i])

    if len(dispositivos)<=10 and len(dispositivos)!=0:
        for i, disp in enumerate(dispositivos):
            if i % 2 == 0:
                columna = 0
                fila_actual += 6
            elif i == 1:
                columna = 5
            else:
                columna = 5

            ttk.Label(frame, text=disp.nombre, font="Times 11").grid(row=fila_actual, column=columna, sticky="w")

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
        ttk.Button(frame, text="Listo", command=lambda: recopilar_informacion(largo_cable, dispositivos, variables_potencia, variables_voltaje, variables_corriente, variables_tiempo)).grid(row=fila_actual + 7, column=0, columnspan=5)
        ttk.Button(frame, text="Atrás", command=main).grid(row=fila_actual + 7, column=1, columnspan=5)
    else:
        ttk.Label(frame, text="Haz seleccionado más de 10 dispositivos o ninguno\nRegresa y selecciona entre 1 y 10 dispositivos", font="Times 8").grid(row=fila_actual +6, column=0, columnspan=10)
        ttk.Button(frame, text="Atrás", command=main).grid(row=fila_actual + 7, column=0, columnspan=10)

def recopilar_informacion(largo_cable, dispositivos, variables_potencia, variables_voltaje, variables_corriente, variables_tiempo):
    for i, dispositivo in enumerate(dispositivos):
            dispositivo.set_seleccion(1)
            dispositivo.set_potencia(variables_potencia[i].get())
            dispositivo.set_voltaje(variables_voltaje[i].get())
            dispositivo.set_corriente(variables_corriente[i].get())
            dispositivo.set_tiempo(variables_tiempo[i].get())

    results(largo_cable, dispositivos)

def results(largo_cable, dispositivos):
    frame = clear_frame()
    tk.Label(frame, text="", font="Times 10").grid(row=1, column=0, columnspan=10)
    costo_total = 0
    corriente_total = 0
    voltaje_total = 0
    nombres = []
    for i, dispositivo in enumerate(dispositivos):
        nombres.append(dispositivo.nombre)
        corriente_total += dispositivo.get_corriente()
        voltaje_total += dispositivo.get_voltaje()
        potencia_calculada = calc.Confirmacion_potencia(dispositivo.get_voltaje(), dispositivo.get_corriente())
        if potencia_calculada != dispositivo.get_potencia():
            ttk.Label(frame, text="Se ha corregido el valor de la potencia en: " + dispositivo.nombre + " a: " + str(potencia_calculada), font="Times 10").grid(row=i+1, column=0, columnspan=10)
        costo_total += calc.calculo_costo(potencia_calculada, dispositivo.get_tiempo(), 30)
    tk.Label(frame, text="Observa los resultados en la nueva pantalla", font="Times 10").grid(row=11, column=0, columnspan=10)
    ttk.Button(frame, text="Atrás", command=main).grid(row=12, column=0, columnspan=10)
    #MOSTRAR RESULTADOS
    calibre = calc.calculo_calibre(corriente_total, largo_cable, voltaje_total)
    texto_calibre = ""
    if calibre == 0:
        texto_calibre = "El diametro es mayor al que este programa calcula, prueba con otros datos"
    else:
        texto_calibre = "El calibre del cable a usar es:" + str(calibre)
    texto_cobro = "Se cobrarán Q." + str(costo_total) + "en el mes"
    tipo_factura = "Esta es una factura de Cobro de Baja Tensión Simple Social - BTSS"

    graficas.mostrar_grafica(nombres, dispositivos, texto_calibre, texto_cobro, tipo_factura)
    
def main():
    frame = clear_frame()
    # Encabezado
    ttk.Label(frame, text="\nEjercicio 5 - Parcial 3 - Física 3", font="Times 10 italic").grid(row=0, column=0, columnspan=15)
    ttk.Label(frame, text="Fabiola Contreras 22787\tMaría José Villafuerte 22129", font="Times 10 italic").grid(row=1, column=0, columnspan=10)
    
    # Título
    ttk.Label(frame, text="¿Qué elementos deseas tomar en consideración?", font="Times 20").grid(row=2, column=0, columnspan=10)
    ttk.Label(frame, text="Selecciona como máximo 10 dispositivos para la simulación, de lo contrario no se completará el proceso", font="Times 8").grid(row=3, column=0, columnspan=10)
    ttk.Label(frame, text="", font="Times 8").grid(row=4, column=0, columnspan=10)

    # Llamar a la función para crear contenido
    seleccion_dispositivos(frame)
    ventana.mainloop()

if __name__ == "__main__":
    main()
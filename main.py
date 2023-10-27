'''
Universidad del Valle de Guatemala
Parcial 3 - Física 3
Energía eléctica
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import tkinter as tk # Libreria para creacion de interfaz grafica
import calc
import graficas

def clear_frame():
    for widgets in Main_page.winfo_children():
      widgets.destroy()

def main():
    clear_frame()
    tk.Label(Main_page, text = "\nEjercicio 5 - Parcial 3 - Física 3", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "Fabiola Contreras 22787\tMaría José Villafuerte 22129\n", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "¿?", font="Times 20").pack()

'''
PUEDE SER UTIL
TEXTO
    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y el disco", font="Times 8").place(x=10, y=140)
SOLICITUD
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=160)
BOTON
    def Call_calculation():
        E = calc.Funcion_ecuacion_CampoE_Disco(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        graficas.Grafica_CampoE_Disco(float(Input_radio.get()), float(Input_Distancia.get()), E)
    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=190)
'''
Main_page = tk.Tk()
Main_page.geometry("650x450")
main()
Main_page.mainloop()


from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

operador = ''  # Para la calculadora
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# Funciones para la calculadora
def click_boton(numero):  # Calculadora: presionar un botón
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)  # Borrar lo que se va presionando desde 0 hasta el final
    visor_calculadora.insert(END, operador)  # Se va a insertar al final (END) y el elemento a insertar


def borrar():  # Calculadora: presionar el botón de borrar (B)
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():  # Calculadora: presionar el botón de resultado (R)
    global operador
    resultado = str(eval(operador))  # str: los widgets en Tkinter suelen esperar strings para mostrar contenido
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


# Función para los checkbox del menú
def revisar_check():
    for c in range(len(cuadros_comida)):  # Por cada comida en el rango de la longitud de los cuadros de comida
        if variables_comida[c].get() == 1:  # variables_comida solo son para marcar 0 o 1 en el checkbox
            cuadros_comida[c].config(state=NORMAL)  # El estado del cuadro va a activarse
            if cuadros_comida[c].get() == '0':  # Si en el cuadro de comida hay un cero
                cuadros_comida[c].delete(0, END)  # Se borra el 0 para que se muestre en blanco
            cuadros_comida[c].focus()  # Colocar el cursor en el cuadro
        else:
            cuadros_comida[c].config(state=DISABLED)
            texto_comida[c].set('0')

    for b in range(len(cuadros_bebida)):
        if variables_bebida[b].get() == 1:
            cuadros_bebida[b].config(state=NORMAL)
            if cuadros_bebida[b].get() == '0':
                cuadros_bebida[b].delete(0, END)
            cuadros_bebida[b].focus()
        else:
            cuadros_bebida[b].config(state=DISABLED)
            texto_bebida[b].set('0')

    for p in range(len(cuadros_postre)):
        if variables_postre[p].get() == 1:
            cuadros_postre[p].config(state=NORMAL)
            if cuadros_postre[p].get() == '0':
                cuadros_postre[p].delete(0, END)
            cuadros_postre[p].focus()
        else:
            cuadros_postre[p].config(state=DISABLED)
            texto_postre[p].set('0')


# Funciones para los botones del panel derecho
def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.16
    total = subtotal + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)  # 1: se refiere a la fila 1   0: se refiere a la columna 0
    num_recibo = f'N# - {random.randint(1000, 9999)}'  # Generar un número de ticket aleatorio
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day:02d}/{fecha.month:02d}/{fecha.year} - {fecha.hour:02d}:{fecha.minute:02d}'
    # :02d formatear el número con dos dígitos, rellenando con ceros a la izquierda si es necesario
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    for id_comida, cant_comida in enumerate(texto_comida):  # enumerate: muestra el índice y el valor
        if cant_comida.get() != '0':  # Si la cantidad de comida es diferente de 0
            cantidad = int(cant_comida.get())  # La cantidad de comida está como str y se cambia a int
            costo = cantidad * precios_comida[id_comida]  # Operación: cantidad * precio
            texto_recibo.insert(END, f'{lista_comidas[id_comida]}\t\t{cantidad}\t${costo:.2f}\n')

    for id_bebida, cant_bebida in enumerate(texto_bebida):
        if cant_bebida.get() != '0':
            cantidad = int(cant_bebida.get())
            costo = cantidad * precios_bebida[id_bebida]
            texto_recibo.insert(END, f'{lista_bebidas[id_bebida]}\t\t{cantidad}\t${costo:.2f}\n')

    for id_postre, cant_postre in enumerate(texto_postre):
        if cant_postre.get() != '0':
            cantidad = int(cant_postre.get())
            costo = cantidad * precios_postres[id_postre]
            texto_recibo.insert(END, f'{lista_postres[id_postre]}\t\t{cantidad}\t${costo:.2f}\n')

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de Postre: \t\t\t{var_costo_postre.get()}\n')

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)  # Obtener el texto completo del recibo
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')  # Cuadro de diálogo para guardar archivo
    archivo.write(info_recibo)  # Escribir el contenido de info_recibo en el archivo abierto
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')  # Mostrar un mensaje de información


def resetear():
    texto_recibo.delete(0.1, END)  # Resetear el recibo

    # Resetear las cantidades del menú
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    # Resetear el estado del cuadro
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    # Resetear los checkbox
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    # Resetear los costos
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Inicia tkinter
aplicacion = Tk()

# Ventana
aplicacion.geometry('1020x630+0+0')  # Tamaño y posición de la ventana
aplicacion.resizable(False, False)  # Evitar maximizar
aplicacion.title('Mi Restaurante - Sistema de Facturación')  # Título
aplicacion.config(bg='#D9754A')  # Cambiar el color de fondo

# Paneles - Superior
panel_superior = Frame(aplicacion)  # Frame: colocar paneles
panel_superior.pack(side=TOP)  # .pack: posicionar el panel, por default se colocan de arriba hacia abajo
# Etiquetas
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', font=('Poppins', 40), fg='#2F302B', bg='#FFDF99',
                        width=25)  # Label: etiqueta para paneles  fg: color del texto
etiqueta_titulo.grid(row=0, column=0)  # Colocar la etiqueta en una cuadrícula, fila y columna

# Paneles - Izquierdo
panel_izquierdo = Frame(aplicacion, bg='#337357', width=500)
panel_izquierdo.pack(side=LEFT, pady=3)
# Costos
panel_costos = Frame(panel_izquierdo, bg='#98B634', padx=35)
panel_costos.pack(side=BOTTOM)
# Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', bg='#337357', relief=FLAT, font=('Raleway', 19, 'bold'),
                           fg='white')
panel_comidas.pack(side=LEFT)
# Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', bg='#337357', relief=FLAT, font=('Raleway', 19, 'bold'),
                           fg='white')
panel_bebidas.pack(side=LEFT)
# Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', bg='#337357', relief=FLAT, font=('Raleway', 19, 'bold'),
                           fg='white')
panel_postres.pack(side=LEFT)

# Paneles - Derecho
panel_derecho = Frame(aplicacion, bg='#4B384C', width=500)
panel_derecho.pack(side=RIGHT, pady=3)
# Calculadora
panel_calculadora = Frame(panel_derecho, relief=FLAT, bg='#4B384C')
panel_calculadora.pack()
# Recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='#4B384C')
panel_recibo.pack()
# Botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='#4B384C')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Carne', 'Kebab', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino1', 'Vino2', 'Cerveza1', 'Cerveza2']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel1', 'Pastel2', 'Pastel3']

# Generar items de comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()  # IntVar: crear variable int que contiene el valor 0 o 1 del checkbutton

    # Crear Checkbuttons
    comida = Checkbutton(panel_comidas, text=comida.title(), bg='#337357', font=('Raleway', 15), onvalue=1, offvalue=0,
                         variable=variables_comida[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)  # sticky=W: se ajusten a la izquierda

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Poppins', 15, 'bold'), width=5, state=DISABLED,
                                     textvariable=texto_comida[contador])
    # Entry: entrada de texto por el usuario
    # state=DISABLED: solo se puede ingresar la cantidad de comida cuando se marque el checkbox
    # textvariable = texto_comida[contador]): asociarlo a esa variable
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items de bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()

    # Crear Checkbuttons
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), bg='#337357', font=('Raleway', 15), onvalue=1, offvalue=0,
                         variable=variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Poppins', 15, 'bold'), width=5, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items de postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()

    # Crear Checkbuttons
    postre = Checkbutton(panel_postres, text=postre.title(), bg='#337357', font=('Raleway', 15), onvalue=1, offvalue=0,
                         variable=variables_postre[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Poppins', 15, 'bold'), width=5, state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text='Costo Comida', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos, text='Costo Bebida', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos, text='Costo Postre', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# Etiqueta de subtotal y campo de entrada
etiqueta_subtotal = Label(panel_costos, text='Subtotal', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiqueta de impuestos y campo de entrada
etiqueta_impuestos = Label(panel_costos, text='Impuestos', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                        textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

# Etiqueta de total y campo de entrada
etiqueta_total = Label(panel_costos, text='Total', fg='white', font=('Dosis', 12, 'bold'), bg='#98B634')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), width=10, state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Raleway', 12, 'bold'), fg='white', bg='#4B384C', bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), width=45, height=8)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), bd=1, width=34)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='#4B384C',
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()

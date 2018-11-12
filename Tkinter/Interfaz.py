import tkinter as tk #Se usa para poder hacer interfaces
import os#Para leer y escribir archivos, manipular directorios

#Se crea la funcion para generar el archivo .txt
def guardar():
    archivo=open("Guardar.txt","w")#Guarar.txt es el nombre y la w es para sobrescribirlo
    archivo.write(entrada.get())#Se guarda en un archivo txt lo que ingresa el usuario

#Se crea la funcion para mostrar el archivo .txt
def mostrar():
    archivoG=open("Guardar.txt")
    return most.set(archivoG.read())

#Se crea la funcion para abrir un archivo .py
def capturar():
    os.system('explorer')

#Se crea la funcion para abrir un archivo .py
def path():
    directorio =os.getcwd()
    return dir.set(directorio)

#Se crea la ventana
ventana =tk.Tk()
ventana.title("Interfaz")
ventana.geometry('400x400')#Ancho=400, alto=300
ventana.configure(background='dark turquoise')

#Guardar
e1=tk.Label(ventana,text="Ingresa texto",bg="pink",fg="grey")#Etiqueta
e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
entrada=tk.Entry(ventana)#Lee
entrada.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
botonGuardar=tk.Button(ventana,text="Guardar",fg="blue",command=guardar)
botonGuardar.pack(side=tk.TOP)

#Mostrar
e2=tk.Label(ventana,text="Ver mensajes",bg="pink",fg="grey")#Etiqueta
e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
most=tk.StringVar()
muestra=tk.Label(ventana,textvariable=most,bg="white",fg="black")#Etiqueta
muestra.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
botonMostrar=tk.Button(ventana,text="Mostrar",fg="blue",command=mostrar)
botonMostrar.pack(side=tk.TOP)

#Abrir archivo de python
e4=tk.Label(ventana,text="Abrir un archivo",bg="pink",fg="grey")#Etiqueta
e4.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
botonCapturar=tk.Button(ventana,text="Abrir",fg="blue",command=capturar)
botonCapturar.pack(side=tk.TOP)

#Path
e3=tk.Label(ventana,text="Path",bg="pink",fg="grey")#Etiqueta
e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
dir=tk.StringVar()
muestraPath=tk.Label(ventana,textvariable=dir,bg="white",fg="black")#Etiqueta
muestraPath.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
botonPath=tk.Button(ventana,text="Path",fg="blue",command=path)
botonPath.pack(side=tk.TOP)

ventana.mainloop()

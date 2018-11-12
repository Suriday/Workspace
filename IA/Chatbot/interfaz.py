from tkinter import *
from tkinter import messagebox  
import os 

class controlPanel():
    #http://pharalax.com/blog/python-desarrollo-de-interfaces-graficas-con-tkinter-labelsbuttonsentrys/
    def __init__(self):
        self.app = Tk()
        self.app.geometry("500x500")
        self.app.title("Asistente Virtual")
        #Pantalla Principal
        self.photo = Frame(self.app)
        self.photo.pack()       
        self.photo.grid(column=0, row=0, padx=(50,50), pady=(10,10))
        self.photo.columnconfigure(0, weight=1)
        self.photo.rowconfigure(0, weight=1) 
        ###########################################
        #Configuracion para la toma de fotos
        #self.label_0 = Label(self.app, text="Tomar foto", width=20, font=("bold", 12))
        #self.label_0.grid(column=2, row=1, sticky=(W,E))

        #entry_1 = Entry(app)
        #entry_1.grid(column=1, row=1)
        """ Configuracion del boton para tomar foto"""
        """, bg='brown', fg='white' """
        btn_photo = Button(self.app, text='Tomar Foto', width=12, command=self.takePicture)
        btn_photo.grid(column=1, row=1)
        """ Configuracion del boton para tomar audio"""
        btn_audio = Button(self.app, text='Hablar',width=12, command=self.speechAudio)
        btn_audio.grid(column=1, row=2)
        """ Escribir notas"""
        btn_notes = Button(self.app, text='Crear notas',width=12, command=self.showNotes)
        btn_notes.grid(column=4, row=1)


        #Iniciar interfaz
        self.app.mainloop()
    def showNotes(self):
        print('Notas')
    def speechAudio(self):
        print('Audio')
    def takePicture(self):
        print('Tomar Foto')

    def execPy(self, archivo):
        os.system('python '+archivo)

def main():
        app = controlPanel()
        return 0

if __name__ == '__main__':
    main()




from tkinter import *
from tkinter import messagebox  
import tkinter as tk
import os 

from tkinter.filedialog import *

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
        ############
        
        ################################################################

        """
        #Creacion de botones en la lista principal 
        btnCreate('Nombre del boton', 'cordenada x', 'cordenada y', 'evento')
        """        
        self.btnCreate(self.app,'Crear notas', 1, 1, self.createNotes)
        self.btnCreate(self.app,'Audio', 1, 2, self.speechAudio)
        self.btnCreate(self.app,'Buscar Foto', 1, 3, self.loadFile)
        
        return self.app.mainloop()

    def btnCreate(self,windows,text,column,row,execMethod):
        """Plantilla para crear botones"""
        btn_notes = Button(windows, text=text,width=12, command=execMethod)
        btn_notes.grid(column=column, row=row)

    def createNotes(self):
        notes = Tk()
        notes.geometry("500x400")
        notes.title('Crear Nota')

        entry = Text(notes)
        entry.place(x=20, y=20, height=300, width=460) 

        btn_save_note = Button(notes, text="Guardar", command=lambda: self.getText((entry.get('1.0','end-1c'))) )
        btn_save_note.place(x=200,y=350,height=30, width=100)
       

    def getText(self, text):
        print(text+ ' '+ str(type(text)))

    def speechAudio(self):
        print('Audio')
        
    def takePicture(self):
        print('Tomar foto')

    def loadFile(self):
        path= askopenfilename(filetypes=( ("Imagenes", "*.jpg; *.jpeg"), ("All files", "*.*") ))
        print('Path: '+path +' ' + str(type(path)))

    def execPy(self, archivo):
        os.system('python '+archivo)

def main():
        return controlPanel()

if __name__ == '__main__':
    main()




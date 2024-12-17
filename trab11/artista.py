import tkinter as tk
from tkinter import messagebox
import album as alb
import artista as art
import playlist as play
from tkinter import simpledialog

class Artista:

    def __init__(self, nome):
        self.__nome = nome
        self.__listaAlbuns = []
        

    def getNome(self):
        return self.__nome

    def getAlbum(self):
        return self.__listaAlbuns


class LimiteMostraArtistas(tk.Toplevel):
    def __init__(self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.configure(bg='#1DB954')
        self.title("Consulta")
        self.controle = controle
        
        self.framenome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framenome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.framenome,text="Nome: ")
        self.labelNome.pack(side="left")  
      
        self.labelnome = tk.Label(self.framenome,text="Ano: ")
      
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side="left")
      
        self.buttonPesquisar = tk.Button(self.frameButton ,text="Pesquisar")      
        self.buttonPesquisar.pack(side="left")
        self.buttonPesquisar.bind("<Button>", controle.pesquisar)  
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteInsereArtistas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)

      
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

      
class CtrlArtista():       
    def __init__(self):
        self.listaMusicas = []
        self.listaArtistas = []
      
    def getListaArtista(self):
       return self.listaArtistas

    def getListaMusicas(self):
       return self.listaMusicas

    def InserirAlbum(self,album,nome):
        print(nome)
        for are in self.getListaArtista(self.CtrlArtista):
          if are.getNome(self.Artista) == nome:
            self.listaAlbuns.append(album)

    def insereArtistas(self):
        self.limiteIns = LimiteInsereArtistas(self) 

    def mostraArtistas(self):
        self.limiteIns = LimiteMostraArtistas(self)
        

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def pesquisar(self,event):
        nome = self.limiteIns.inputnome.get()
        
        str = 'Código -- Nome\n'
        str += nome
        for disc in self.listaArtistas:
          if disc.getNome is nome:
            for music in self.listaMusicas:
              str += disc.getNome + ' -- ' + disc.getAlbum + '\n'
              self.limiteLista = LimiteMostraArtistas(str)
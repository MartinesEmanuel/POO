import tkinter as tk
from tkinter import messagebox
import album as alb
import artista as art
import playlist as play

class Musica():
  def __init__(self, titulo, nroFaixas):
      self.__titulo = titulo
      self.__nroFaixa = nroFaixas
    
  @property
  def titulo(self):
      return self.__titulo
    
  @property
  def nroFaixas(self):
      return self.__nroFaixas


class Album():
    def __init__(self, titulo, ano, musicas):
        self.__titulo = titulo
        self.__ano = ano
        self.__musicas = musicas

    @property
    def titulo(self):
        return self.__titulo
      
    @property
    def ano(self):
        return self.__ano
      
    @property
    def musicas(self):
        return self.__musicas

class LimiteMostraAlbum(tk.Toplevel):
    def __init__(self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.configure(bg='#1DB954')
        self.title("Nome a ser pesquisado")
        self.controle = controle
        
        self.framenome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framenome.pack()
        self.frameButton.pack()
      
        self.labelnome = tk.Label(self.framenome,text="Ano: ")
      
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side="left")
      
        self.buttonPesquisar = tk.Button(self.frameButton ,text="Pesquisar")      
        self.buttonPesquisar.pack(side="left")
        self.buttonPesquisar.bind("<Button>", controle.pesquisar)  
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
      
class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.configure(bg='#1DB954')
        self.title("Album")
        self.controle = controle

        self.framenome = tk.Frame(self)
        self.frametitulo = tk.Frame(self)
        self.frameano = tk.Frame(self)
        self.framemusicatitulo = tk.Frame(self)
        self.framemusicaNroFaixa = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framenome.pack()
        self.frameano.pack()
        self.frametitulo.pack()
        self.frameButton.pack()
        self.framemusicaNroFaixa.pack()
        self.framemusicatitulo.pack()
      
        self.labelnome = tk.Label(self.framenome,text="Nome: ")
        self.labelano = tk.Label(self.frameano,text="Ano: ")
        self.labeltitulo = tk.Label(self.frametitulo,text="Titulo: ")
        self.labelmusicatitulo = tk.Label(self.framemusicatitulo,text="Título Musica: ")
        self.labelmusicaNroFaixa = tk.Label(self.framemusicaNroFaixa,text="Faixa Musica: ")
        self.labelano.pack(side="left")
        self.labeltitulo.pack(side="left")  
        self.labelmusicatitulo.pack(side="left")  
        self.labelmusicaNroFaixa.pack(side="left")  
        self.labelnome.pack(side="left")
      
        self.inputano = tk.Entry(self.frameano, width=20)
        self.inputano.pack(side="left")
        self.inputtitulo = tk.Entry(self.frametitulo, width=20)
        self.inputtitulo.pack(side="left")             
        self.inputmusicatitulo = tk.Entry(self.framemusicatitulo, width=20)
        self.inputmusicatitulo.pack(side="left")     
        self.inputmusicaNroFaixa = tk.Entry(self.framemusicaNroFaixa, width=20)
        self.inputmusicaNroFaixa.pack(side="left") 
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side="left") 
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

        self.buttonMusica = tk.Button(self.frameButton ,text="InsereMúsica")      
        self.buttonMusica.pack(side="left")
        self.buttonMusica.bind("<Button>", controle.MusicaHandler)
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraaAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de musicas', str)
    
      
class CtrlAlbum():       
    def __init__(self):
        self.listaAlbum = [
            Album('COM220', 'Programação OO',[Musica("oi","a"),Musica("q","h")]),
            Album('COM222', 'Programação Web',[Musica("oi","a"),Musica("q","h")]),
            Album('COM111', 'Estruturas de Dados',[Musica("oi","a"),Musica("q","h")])
        ]
        self.listaMusica = []
      
  
    def getListaMusicas(self):
        return self.listaMusica
      
    def getListaAlbum(self):
        return self.listaAlbum

    def getListaCodAlbum(self):
        listaCod = []
        for al in self.listaAlbum:
            listaCod.append(al.ano)
        return listaCod

    def insereAlbum(self):
        self.limiteIns = LimiteInsereAlbum(self) 

    def mostraAlbum(self):
        self.limiteIns = LimiteMostraAlbum(self)
        
        
    def salvaHandler(self, event):
        self.nome = self.view.inputText1.get()

    def enterHandler(self, event):
        ano = self.limiteIns.inputano.get()
        titulo = self.limiteIns.inputtitulo.get()
        nome = self.limiteIns.inputnome.get()
        musicas =  self.getListaMusicas()
        album = Album(ano, titulo, musicas)
        listaArtistas = art.CtrlArtista.getListaArtista(self)
        for are in listaArtistas:
          if are.getNome(self.Artista) == nome:
            are.listaAlbuns.append(album)
        self.limiteIns.mostraJanela('Sucesso', 'Album cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputano.delete(0, len(self.limiteIns.inputano.get()))
        self.limiteIns.inputtitulo.delete(0, len(self.limiteIns.inputtitulo.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def MusicaHandler(self, event):
        musicatitulo = self.limiteIns.inputmusicatitulo.get()
        musicaNroFaixas = self.limiteIns.inputmusicaNroFaixa.get()
        self.listaMusica.append(Musica(musicatitulo,musicaNroFaixas))

    def pesquisar(self,event):
        nome = self.limiteIns.inputnome.get()
        
        str = 'Código -- Nome\n'
        str += nome
        for disc in self.listaAlbum:
          
            str += disc.ano + ' -- ' + disc.titulo + '\n'
        self.limiteLista = LimiteMostraaAlbum(str)
        self.clearHandler(event)
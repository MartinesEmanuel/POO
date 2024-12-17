import tkinter as tk
from tkinter import messagebox
import album as alb
import artista as art
import playlist as play

class Playlist:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

#artista ARtista album Album playlist Playlist
class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtista, listaMusica):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        self.frameNomePlaylist = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNomePlaylist.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()        

        self.labelNomePlaylist = tk.Label(self.frameNomePlaylist,text="Informe o nome: ")
        self.labelNomePlaylist.pack(side="left")
        self.inputNomePlaylist = tk.Entry(self.frameNomePlaylist, width=20)
        self.inputNomePlaylist.pack(side="left")

        self.labeArtista = tk.Label(self.frameArtista,text="Escolha Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = tk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtista
          
        self.labelEst = tk.Label(self.frameMusica,text="Escolha Musica: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusica)
        self.listbox.pack(side="left")
        for nro in listaMusica:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Musica")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraPlaylist():
    def __init__(self, str):
        messagebox.showinfo('Lista de Playlist', str)

class CtrlPlaylist():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylist = []

    def inserePlaylists(self):        
        self.listaMusica = []
        listaArtista = self.ctrlPrincipal.ctrlArtista.getListaArtista()
        listaMusica = self.ctrlPrincipal.ctrlAlbum.getListaMusicas()
        self.limiteIns = LimiteInserePlaylist(self, listaArtista, listaMusica)

    def criaPlaylist(self, event):
        NomePlaylist = self.limiteIns.inputNomePlaylist.get()
        artistaSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlArtista.getListaArtista(artistaSel)
        playlist = Playlist(NomePlaylist, self.listaMusica)
        self.listaMusica.append(musica) #BATATA AQUI TA QUEIMANDO
        self.limiteIns.mostraJanela('Sucesso', 'playlist criada com sucesso')
        self.limiteIns.destroy()

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSel)
        self.MusicaPlaylist.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica Adicionada')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraPlaylist(self):
        str = ''
        for playlist in self.listaPlaylist:
            str += 'NomePlaylist: ' + playlist.nome + '\n'
            
            str += 'Musicas:\n'
            for Musica in playlist.Musica:
                str += Musica.nome + ' - ' + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraPlaylist(str)
    
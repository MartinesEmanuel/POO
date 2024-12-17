import tkinter as tk
from tkinter import messagebox
import album as alb
import artista as art
import playlist as play

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('720x420')
        self.root.configure(bg='#1DB954')
        self.menubar = tk.Menu(self.root)        
        self.ArtistaMenu = tk.Menu(self.menubar)
        self.AlbumMenu = tk.Menu(self.menubar)
        self.PlaylistMenu = tk.Menu(self.menubar)     
        
        self.ArtistaMenu.add_command(label="Insere", \
                    command=self.controle.insereArtistas)
        self.ArtistaMenu.add_command(label="Mostra", \
                    command=self.controle.mostraArtistas)
        self.menubar.add_cascade(label="Artista", \
                   menu=self.ArtistaMenu)

        self.AlbumMenu.add_command(label="Insere", \
                    command=self.controle.insereAlbum)
        self.AlbumMenu.add_command(label="Mostra", \
                    command=self.controle.mostraAlbum)  
        self.menubar.add_cascade(label="Album", \
                    menu=self.AlbumMenu)

        self.PlaylistMenu.add_command(label="Insere", \
                    command=self.controle.inserePlaylists)
        self.PlaylistMenu.add_command(label="Mostra", \
                    command=self.controle.mostraPlaylists)                     
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.PlaylistMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum()
        self.ctrlPlaylist = play.CtrlPlaylist(self)
      
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Spotify")
        self.root.mainloop()
      
    def insereArtistas(self):
        self.ctrlArtista.insereArtistas()

    def mostraArtistas(self):
        self.ctrlArtista.mostraArtistas()

    def insereAlbum(self):
        self.ctrlAlbum.insereAlbum()

    def mostraAlbum(self):
        self.ctrlAlbum.mostraAlbum()

    def inserePlaylists(self):
        self.ctrlPlaylist.inserePlaylists()

    def mostraPlaylists(self):
        self.ctrlPlaylist.mostraPlaylists()

    def insereMusicas(self):
        self.isereMusicas()

if __name__ == '__main__':
    c = ControlePrincipal()
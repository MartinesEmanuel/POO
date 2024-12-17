import tkinter as tk
from tkinter import messagebox
import futebol as fut


class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('1200x720')
        self.root.configure(bg='black')
        self.menubar = tk.Menu(self.root)
        self.JogosMenu = tk.Menu(self.menubar)
        self.JogosMenu1 = tk.Menu(self.menubar)
        self.JogosMenu2 = tk.Menu(self.menubar)
        self.JogosMenu3 = tk.Menu(self.menubar)

        self.JogosMenu.add_command(label="insereCurso", \
                                   command=self.controle.insereCurso)
        self.JogosMenu.add_command(label="Insere Equipe", \
                                   command=self.controle.insereEstudante)
        self.menubar.add_cascade(label="Cadastrar", \
                                 menu=self.JogosMenu)

        self.JogosMenu1.add_command(label="Criar equipe", \
                                   command=self.controle.criarEquipe)
        self.menubar.add_cascade(label="Equipe", \
                                 menu=self.JogosMenu1)

        self.JogosMenu2.add_command(label="Consultar equipe", \
                                   command=self.controle.ConsultarEquipe)
        self.menubar.add_cascade(label="Consultar equipe", \
                                 menu=self.JogosMenu2)

        self.JogosMenu3.add_command(label="Dados do campeonato", \
                                   command=self.controle.DadosEquipe)
        self.menubar.add_cascade(label="Imprimir dados", \
                                 menu=self.JogosMenu3)

        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlFutebol = fut.CtrlFutebol(self)

        self.ctrlFutebol.carregar_dados()
        self.ctrlFutebol.iniciar()
        self.limite = LimitePrincipal(self.root, self)

        self.root.protocol("WM_DELETE_WINDOW", self.fecharPrograma)

        self.root.title("InterClasse Futebol")
        self.root.mainloop()

    def insereCurso(self):
        self.ctrlFutebol.inserecurso()

    def insereEstudante(self):
        self.ctrlFutebol.insereestudante()

    def criarEquipe(self):
        self.ctrlFutebol.criarequipe()

    def ConsultarEquipe(self):
        self.ctrlFutebol.consultarEquipe()

    def DadosEquipe(self):
        self.ctrlFutebol.dadosEquipe()

    def fecharPrograma(self):
        self.ctrlFutebol.salvar_dados()  # Salva os dados antes de fechar o programa
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()

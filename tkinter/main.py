import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class ModelCliente():
    def __init__(self, nome, email,codigo):
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def codigo(self):
        return self.__codigo

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()

        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.labelInfo1 = tk.Label(self.frame1, text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3, text='Código:')
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")
        self.labelInfo3.pack(side='left')

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")

        self.buttonSubmit = tk.Button(self.janela, text="Salva")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)

        self.buttonClear = tk.Button(self.janela, text="Limpa")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonConsult = tk.Button(self.janela, text='Consulta')
        self.buttonConsult.pack(side="left")
        self.buttonConsult.bind("<Button>",controller.consultHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def mostraJanelaErro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)
    def mostraJanelaDados(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)



class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x200')
        self.root.configure(background="#1e3743")
        self.root.resizable(True,True)
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self)

        self.root.title("ATV-Tkinter01")
        # Inicia o mainloop
        self.root.mainloop()

    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codiCli  = self.view.inputText3.get()
        for i in self.listaClientes:
            if i.codigo == codiCli:
                self.view.mostraJanelaErro('Erro', 'Código já existente')
                return
        cliente = ModelCliente(nomeCli,emailCli,codiCli)

        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def consultHandler(self,event):
        code = simpledialog.askstring("Código","Digite o código:",parent=self.root)
        for i in self.listaClientes:
            if code == i.codigo:
                self.view.mostraJanela("Dados",f"Nome:  {i.nome}\nEmail:  {i.email}")
            return
        self.view.mostraJanela("Erro","Código não cadastrado.")


if __name__ == '__main__':
    c = Controller()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Curso:
    def __init__(self,sigla, nome):
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla

    @property
    def nome(self):
        return self.__nome

class Estudante:
    def __init__(self, nroMatricula,nome,curso):
        self.__nroMatricula = nroMatricula
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatricula(self):
        return self.__nroMatricula

    @property
    def nome(self):
        return self.__nome

    @property
    def curso(self):
        return self.__curso


class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("InterCamp")
        self.controle = controle

        self.frameSigla = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameSigla.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameSigla, text="Sigla: ")
        self.labelTitulo = tk.Label(self.frameNome, text="Nome: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameSigla, width=10)
        self.inputTitulo = tk.Entry(self.frameNome, width=20)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereEstudante(tk.Toplevel):
    def __init__(self, controle, cursos):
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("InterCamp")
        self.controle = controle

        self.framenroMat = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroMat.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroMat, text="Nro Matricula: ")
        self.labelTitulo = tk.Label(self.frameNome, text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso, text="Curso")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelCurso.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroMat, width=10)
        self.comboCurso = ttk.Combobox(self.frameCurso, values=[curso.sigla for curso in cursos], width=20)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.comboCurso.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler1)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler1)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler1)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteCriarEquipe(tk.Toplevel):
    def __init__(self, controle, cursos):
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("InterCamp")
        self.controle = controle

        self.framenroMat = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroMat.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCurso = tk.Label(self.frameCurso, text="Curso")
        self.labelCodigo = tk.Label(self.framenroMat, text="Nro Matricula: ")
        self.labelCodigo.pack(side="left")
        self.labelCurso.pack(side="left")

        self.comboCurso = ttk.Combobox(self.frameCurso, values=[curso.sigla for curso in cursos], width=20)
        self.inputCodigo = tk.Entry(self.framenroMat, width=10)

        self.comboCurso.pack(side="left")
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler2)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler2)

        self.buttonFecha = tk.Button(self.frameButton, text="Finalizar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.finalizaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("InterCamp")
        self.controle = controle


        self.framenroMat = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroMat.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroMat, text="Sigla: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroMat, width=10)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler3)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler3)

        self.buttonFecha = tk.Button(self.frameButton, text="Finalizar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler2)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20, width=40)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteDadosEquipe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('720x420')
        self.title("InterCamp")
        self.controle = controle

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler4)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler4)

        self.buttonFecha = tk.Button(self.frameButton, text="Finalizar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler4)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20, width=40)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)


class CtrlFutebol():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaAuxiliar = []
        self.listaEquipes = []
        self.listaCurso = []
        self.listaEstudante = []

    def inserecurso(self):
        self.limiteCur =  LimiteInsereCurso(self)

    def insereestudante(self):
        self.limiteEst = LimiteInsereEstudante(self, self.listaCurso)

    def criarequipe(self):
         self.limiteEqui = LimiteCriarEquipe(self, self.listaCurso)

    def consultarEquipe(self):
        self.limiteConEqui = LimiteConsultaEquipe(self)
    def dadosEquipe(self):
        self.limiteDad = LimiteDadosEquipe(self)

    def enterHandler(self, event):

        sigla = self.limiteCur.inputCodigo.get()
        nome = self.limiteCur.inputTitulo.get()

        curso = Curso(sigla,nome)
        self.listaCurso.append(curso)
        self.limiteCur.mostraJanela('Sucesso', 'Jogos cadastrado com sucesso')
        self.clearHandler(event)

    def enterHandler1(self, event):

        nroMatri = self.limiteEst.inputCodigo.get()
        nome = self.limiteEst.inputNome.get()
        curso = self.limiteEst.comboCurso.get()

        estudante = Estudante(nroMatri,nome,curso)
        self.listaEstudante.append(estudante)
        self.limiteEst.mostraJanela('Sucesso', 'Jogos cadastrado com sucesso')
        self.clearHandler1(event)

    def enterHandler2(self, event):
        nroMatri = self.limiteEqui.inputCodigo.get()
        curso = self.limiteEqui.comboCurso.get()
        print(nroMatri)
        print(curso)
        estudante_encontrado = False
        for estudante in self.listaEstudante:
            print(f'a{estudante.curso}{curso}a')
            print(f'a{estudante.nroMatricula}{nroMatri}a')
            if str(estudante.curso) == str(curso) and str(estudante.nroMatricula) == str(nroMatri):
                estudante_encontrado = True
                break
        try:
            if estudante_encontrado:
                self.listaAuxiliar.append(nroMatri)
                self.limiteEqui.inputCodigo.delete(0, len(nroMatri))
            else:
                raise ValueError("O número de matrícula não pertence ao curso selecionado.")
        except ValueError as error:
            messagebox.showerror("Erro", str(error))

    def enterHandler3(self, event):
        sigla = self.limiteConEqui.inputCodigo.get()
        # Verifica se a sigla existe na lista de cursos
        curso_encontrado = None
        for curso in self.listaCurso:
            print(f'{curso.sigla} {sigla}')
            if str(curso.sigla) == str(sigla):
                curso_encontrado = curso
                break

        if curso_encontrado is None:
            # Sigla de curso não existe
            self.limiteConEqui.textJogos.config(state=tk.NORMAL)
            self.limiteConEqui.textJogos.delete(1.0, tk.END)
            self.limiteConEqui.textJogos.insert(tk.END, "Esta sigla de curso não existe")
            self.limiteConEqui.textJogos.config(state=tk.DISABLED)
            self.limiteConEqui.textJogos.update()
        else:
            # Verifica se existe equipe do curso
            equipe_encontrada = None
            for equipe in self.listaEquipes:
                print(f'{str(equipe[0])} {str(curso_encontrado.sigla)}')
                if str(equipe[0]) == str(curso_encontrado.sigla):
                    equipe_encontrada = equipe[0]
                    break

            if equipe_encontrada is None:
                # Não existe equipe desse curso
                self.limiteConEqui.textJogos.config(state=tk.NORMAL)
                self.limiteConEqui.textJogos.delete(1.0, tk.END)
                self.limiteConEqui.textJogos.insert(tk.END, "Não existe equipe desse curso")
                self.limiteConEqui.textJogos.config(state=tk.DISABLED)
                self.limiteConEqui.textJogos.update()
            else:
                # Exibe os nomes dos alunos cadastrados na equipe
                self.limiteConEqui.textJogos.config(state=tk.NORMAL)
                self.limiteConEqui.textJogos.delete(1.0, tk.END)
                for equipe in self.listaEquipes:
                    if str(equipe[0]) == str(curso_encontrado.sigla):
                        alunos = equipe[1]
                        self.limiteConEqui.textJogos.insert(tk.END, f"Curso: {curso_encontrado.nome}\n")
                        for matricula in alunos:
                            # Procura o aluno correspondente na lista de estudantes
                            aluno_encontrado = next(
                                (estudante for estudante in self.listaEstudante if str(estudante.nroMatricula) == str(matricula)),
                                None)
                            if aluno_encontrado:
                                self.limiteConEqui.textJogos.insert(tk.END,
                                                                    f"Nome: {aluno_encontrado.nome}, Matrícula: {aluno_encontrado.nroMatricula}\n")
                        break
                self.limiteConEqui.textJogos.config(state=tk.DISABLED)

            self.clearHandler3(event)

    def enterHandler4(self,event):
        # Número de equipes
        numero_equipes = len(self.listaEquipes)

        # Número total de estudantes
        numero_estudantes = sum(len(equipe[1]) for equipe in self.listaEquipes)

        # Média de estudante por equipe
        if numero_equipes > 0:
            media_estudante_equipe = numero_estudantes / numero_equipes
        else:
            media_estudante_equipe = 0

        # Limpar conteúdo da caixa de texto
        self.limiteDad.textJogos.config(state=tk.NORMAL)
        self.limiteDad.textJogos.delete(1.0, tk.END)

        # Exibir informações na caixa de texto
        self.limiteDad.textJogos.insert(tk.END, f"Número de equipes: {numero_equipes}\n")
        self.limiteDad.textJogos.insert(tk.END, f"Número total de estudantes: {numero_estudantes}\n")
        self.limiteDad.textJogos.insert(tk.END, f"Média de estudante por equipe: {media_estudante_equipe}\n")

        self.limiteDad.textJogos.config(state=tk.DISABLED)

    def clearHandler(self,event):
        self.limiteCur.inputCodigo.delete(0, len(self.limiteCur.inputCodigo.get()))
        self.limiteCur.inputTitulo.delete(0, len(self.limiteCur.inputTitulo.get()))

    def clearHandler1(self,event):
        self.limiteEst.inputCodigo.delete(0, len(self.limiteEst.inputCodigo.get()))
        self.limiteEst.inputNome.delete(0, len(self.limiteEst.inputNome.get()))

    def clearHandler2(self,event):
        self.limiteEqui.inputCodigo.delete(0, len(self.limiteEqui.inputCodigo.get()))
        self.limiteEqui.comboCurso.set('')

    def clearHandler3(self,event):
        self.limiteConEqui.inputCodigo.delete(0, len(self.limiteConEqui.inputCodigo.get()))

    def clearHandler4(self,event):
        self.limiteDad.textJogos.config(state=tk.NORMAL)
        self.limiteDad.textJogos.delete(1.0, tk.END)
        self.limiteDad.textJogos.config(state=tk.DISABLED)

    def fechaHandler(self,event):
        self.limiteCur.destroy()

    def fechaHandler1(self,event):
        self.limiteEst.destroy()

    def fechaHandler2(self,event):
        self.limiteConEqui.destroy()

    def fechaHandler3(self,event):
        self.limiteDad.destroy()

    def fechaHandler4(self,event):
        self.limiteDad.destroy()
    def finalizaHandler(self, event):
        curso = self.limiteEqui.comboCurso.get()
        copia_auxiliar = self.listaAuxiliar.copy()

        if not self.listaEquipes:
            self.listaEquipes.append((curso, copia_auxiliar))
            self.listaAuxiliar.clear()
            self.clearHandler2(event)
            messagebox.showinfo("Equipe Formada", "Equipe formada com sucesso para este curso.")
        else:
            try:
                equipe_existente = next(equipe for equipe in self.listaEquipes if equipe[0] == curso)
                messagebox.showinfo("Equipe Existente", "Já foi formada uma equipe para este curso.")
            except StopIteration:
                self.listaEquipes.append((curso, copia_auxiliar))
                self.listaAuxiliar.clear()
                self.clearHandler2(event)
                messagebox.showinfo("Equipe Formada", "Equipe formada com sucesso para este curso.")


    def salvar_dados(self):
        with open('dados.txt', 'w') as arquivo:
            for equipe in self.listaEquipes:
                linha = f"{equipe[0]}: {' '.join(equipe[1])}\n"
                arquivo.write(linha)

    def carregar_dados(self):
        self.listaEquipes.clear()
        with open('dados.txt', 'r') as arquivo:
            for linha in arquivo.readlines():
                dados = linha.strip().split(': ')
                curso = dados[0]
                estudantes = dados[1].split()
                self.listaEquipes.append((curso, estudantes))

    def iniciar(self):
        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)

        self.listaEstudante.append(Estudante(1001, "José da Silva", c1.sigla))
        self.listaEstudante.append(Estudante(1002, "João de Souza", c1.sigla))
        self.listaEstudante.append(Estudante(1003, "Rui Santos", c2.sigla))
        self.listaEstudante.append(Estudante(1004, "Maria Souza", c1.sigla))
        self.listaEstudante.append(Estudante(1005, "Pedro Oliveira", c1.sigla))
        self.listaEstudante.append(Estudante(1006, "Ana Pereira", c2.sigla))
        self.listaEstudante.append(Estudante(1007, "Carlos Mendes", c2.sigla))
        self.listaEstudante.append(Estudante(1008, "Mariana Santos", c1.sigla))
        self.listaEstudante.append(Estudante(1009, "Paulo Andre Custodio", c2.sigla))
        self.listaEstudante.append(Estudante(1010, "Camila Monferrari", c1.sigla))
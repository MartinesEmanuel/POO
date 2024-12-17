from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,endereco,idade,cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf =  cpf

        @property
        def nome(self):
            return self.__nome

        @property
        def endereco(self):
            return self.__endereco

        @property
        def idade(self):
            return self.__idade

        @property
        def cpf(self):
            return self.__cpf

        def printDescricao(self):
            pass

class Professor(Pessoa):
    def __int__(self,nome,endereco,idade,cpf,titulacao):
        super().__int__(nome,endereco,idade,cpf)
        self.__titulacao = titulacao

        @property
        def titulacao(self):
            return  self.__titulacao

        def printDescricao(self):
            print(f"Professor:{self.__nome}\nIdade:{self.__idade}")
            print(f"CPF:{self.__cpf}\nEndereço:{self.__endereco}")
            print(f"Titulação:{self.__titulacao}")

class Aluno(Pessoa):
    def __init__(self,nome,endereco,idade,cpf,curso):
        super().__init__(nome,endereco,idade,cpf)
        self.__curso = curso

        @property
        def curso(self):
            self.__curso

        def printDescricao(self):
            print(f"Aluno:{self.__nome}\nIdade:{self.__idade}")
            print(f"CPF:{self.__cpf}\nEndereço:{self.__endereco}")
            print(f"Curso:{self.__curso}")

class TipoErrado(Exception):
    pass

class IdadeBaixa(Exception):
    pass

class CPFJaExistente(Exception):
    pass

    if _name_ == "_main_":
        listaDePessoas = [
            ("Jane", "6776", "Moc", 53, "Doutor"),  # codinção correta
            ("Wellington", "3289", "Itajuba", 30, "Doutor"),  # codinção correta
            ("Karla", "6842", "Itajuba", 49, "Mestrado"),  # titulação errada
            ("Tiago", "1795", "Moc", 27, "Doutor"),  # idade errada
            ("Heloi", "8493", "Moc", 23, "Graduado"),  # titulação e idade erradas
            ("Warley", "3289", "Itajuba", 47, "Doutor"),  # CPF igual
            ("Pedro", "0000", "Itajuba", 18, "CCO"),  # codinção correta
            ("Lucca", "1274", "Moc", 22, "SIN"),  # codinção correta
            ("Luiza", "7219", "Moc", 16, "CCO"),  # idade errada
            ("Laura", "0916", "Itajuba", 19, "BCO"),  # curso correto
            ("Renato", "2856", "Moc", 17, "EMC"),  # curso e idade errada
            ("Jão", "0000", "Moc", 23, "CCO")  # CPF igual
        ]

        cadastro = []
        for nome, cpf, endereco, idade, tipo in listaDePessoas:
            try:
                if tipo != "Doutor" and tipo != "CCO" and tipo != "SIN":
                    raise TipoErrado
                if tipo == "Doutor" and idade < 30:
                    raise IdadeBaixa
                if tipo == "CCO" and idade < 18:
                    raise IdadeBaixa
                for CPF in cadastro:
                    if cpf == CPF.getCPF:
                        raise CPFJaExistente

                if tipo == "Doutor" and idade >= 30:
                    cadastro.append(Professor(nome, cpf, endereco, idade, tipo))
                if tipo == "CCO" or tipo == "SIN" and idade >= 18:
                    cadastro.append(Aluno(nome, cpf, endereco, idade, tipo))

            except TipoErrado:
                print(f"O tipo de {nome}, {tipo}, não condiz com a que é requerido.")
                print()
            except IdadeBaixa:
                print(f"A idade de {nome} é baixa.")
                print()
            except CPFJaExistente:
                print(f"O CPF {cpf} de {nome} já existe.")
                print()

        for alguem in cadastro:
            alguem.printDescricao()
            print()


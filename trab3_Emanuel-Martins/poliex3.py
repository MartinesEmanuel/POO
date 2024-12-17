from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horas_por_semana, valor_da_hora):
        super().__init__(nome, telefone)
        self.horas_por_semana = horas_por_semana
        self.valor_da_hora = valor_da_hora

    def getSalario(self):
        return self.horas_por_semana * self.valor_da_hora * 4.5

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, dias_por_semana, valor_do_dia):
        super().__init__(nome, telefone)
        self.dias_por_semana = dias_por_semana
        self.valor_do_dia = valor_do_dia

    def getSalario(self):
        return self.dias_por_semana * self.valor_do_dia * 4.5

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valor_do_salario):
        super().__init__(nome, telefone)
        self.valor_do_salario = valor_do_salario

    def getSalario(self):
        return self.valor_do_salario

# Criando as instâncias de empregadas
empregadas = [
    Horista("Maria", "1111-1111", 160, 12),
    Diarista("Joana", "2222-2222", 20, 65),
    Mensalista("Ana", "3333-3333", 1200),
]

# Imprimindo o salário de cada uma
for empregada in empregadas:
    print(f"{empregada.nome}: R$ {empregada.getSalario():.2f}")

# Imprimindo a opção mais barata
salarios = [empregada.getSalario() for empregada in empregadas]
opcao_mais_barata = empregadas[salarios.index(min(salarios))]
print(f"Opção mais barata: {opcao_mais_barata.nome} ({opcao_mais_barata.telefone}), R$ {opcao_mais_barata.getSalario():.2f}")

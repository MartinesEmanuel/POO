from abc import ABC, abstractmethod
from datetime import date


class Conta(ABC):
    def __init__(self,nroConta,nomeCorrentista,saldo):
        self.__nroConta = nroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo 
        self.__transicoes = []
        
        
    
    @property
    def nroConta(self):
        return self.__nroConta
    
    @property
    def nomeCorrentista(self):
        return self.__nomeCorrentista
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def transicoes(self):
        return self.__transicoes
    
  
    def Deposito(self, valor, descricao):
       pass
    
    @abstractmethod
    def retirada(self,valor,descricao =''):
        pass
    
    @abstractmethod
    def imprimir_extrato(self):
        pass
    
class Transacao:
    def __init__(self, data, valor, descricao):
        self.data = data
        self.valor = valor
        self.descricao = descricao
   
    
    
class ContaComum(Conta):
    def __init__(self, nroConta, nomeCorrentista, saldo):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__saldo = saldo
    

    
    def retirada(self, valor, descricao=''):
        if self.__saldo >= valor:
            self.__saldo -= valor 
            self.transicoes.append(Transacao(date.today(), -valor, descricao))
        else:
            print("Saldo Insuficiente")
    
    def imprimir_extrato(self):
        print(f'Conta: {self.nroConta} - Correntista: {self.nomeCorrentista}')
        for transacao in self.transicoes:
            print(f'{transacao.data} - {transacao.descricao}: {transacao.valor:.2f}')
        print(f'Saldo atual: {self.saldo:.2f}')
        
        
class ContaLimite(Conta):
    def __init__(self, nroConta, nomeCorrentista, saldo,limite):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__limite = limite
        self.__saldo = saldo
    
    @property
    def limite(self):
        return self.__limite
    
    def retirada(self, valor, descricao=''):
        if self.__saldo - valor - valor < self.__limite:
            print("Limite de crédito excedido")
        else:
            self.__saldo -= valor
            self.transicoes.append(Transacao(date.today(), -valor, descricao))
            
     
    def imprimir_extrato(self):
        print(f'Conta: {self.nroConta} - {self.nomeCorrentista}')
        print('Transações:')
        for t in self.transicoes:
            if t.valor < 0:
                print(f'{t.data} - Débito - {t.descricao}: R${-t.valor:.2f}')
            else:
                print(f'{t.data} - Crédito - {t.descricao}: R${t.valor:.2f}')
        print(f'Saldo: R${self.saldo:.2f}')
        print(f'Limite de crédito: R${self.limite:.2f}')       
            
class ContaPoupanca(Conta):
    def __init__(self, nroConta, nomeCorrentista, saldo,aniversario):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__aniversario = aniversario
        self.__saldo = saldo
        
    @property
    def aniversario(self):
        return self.__aniversario
    
    def Deposito(self, valor, descricao):
        juros = 0.1 * self.__saldo
        self.__saldo += valor + juros
        self.transicoes.append(Transacao(date.today(), valor, descricao))
    
    def retirada(self, valor, descricao=''):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.transicoes.append(Transacao(date.today(), -valor, descricao))
        else:
            print("Saldo insuficiente")



    def imprimir_extrato(self):
        print("Número da conta:", self.nroConta)
        print("Nome do correntista:", self.nomeCorrentista)
        print("Dia do aniversário:", self.__dia_aniversario)
        print("Transações:")
        for t in self.transicoes:
            print("-", t.data.strftime('%d/%m/%Y'), t.descricao, "R$", t.valor)
        print("Saldo:", "R$", self.saldo)     
    




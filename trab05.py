from abc import ABC, abstractmethod


class Vendedor(ABC):
    def __init__(self,codigo, nome, vendas=None ):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []  

    @property
    def getCodigo(self):
        return self.__codigo
        
    
    @property
    def getVendas(self):
        return self.__vendas
    
    @property
    def getNome(self):
        return self.__nome
    
  
    def adicionaVenda(self,pCodImovel, pMes, pAno, pValor):
       nova_venda = Venda(pCodImovel, pMes, pAno, pValor)
       self.__vendas.append(nova_venda)
        
    @abstractmethod
    def getDados(self):
       pass
   
    @abstractmethod
    def calculaRenda(self, pMes, pAno):
        pass
    
class Venda:
    def __init__(self,codImovel, mesVenda,anoVenda,valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda
        pass  
    
    @property
    def CodImovel(self):
        return self.__codImovel
    
    @property
    def MesVenda(self):
        return self.__mesVenda
    
    @property
    def AnoVenda(self):
        return self.__anoVenda
    
    @property
    def ValorVenda(self):
        return self.__valorVenda
    
    
class Contratado(Vendedor):
    def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho,vendas=None):
        super().__init__(codigo, nome, [])
        self.__nroCartTrabalho = nroCartTrabalho
        self.__salarioFixo = salarioFixo
        self.__nome = nome
        self.__vendas = []
    
       
    @property
    def NroCartTrabalho(self):
        return self.__nroCartTrabalho
    
    @property
    def SalarioFixo(self):
        return self.__salarioFixo
    
    
    def getDados(self):
        print(f"Nome{self.__nome} - Nro Carteira:{self.__nroCartTrabalho}")
        pass
         
        
    def calculaRenda(self, pMes, pAno):
        vendas_mes_ano = [v for v in self._Vendedor__vendas if v.MesVenda == pMes and v.AnoVenda == pAno]
        total_vendas = sum(v.ValorVenda for v in vendas_mes_ano)
        renda = self.__salarioFixo + (0.01 * total_vendas)
        return renda



        
        
class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao, vendas=None):
        super().__init__(codigo, nome, vendas)
        self.__nroCPF = nroCPF
        self.__comissao = comissao
        self.__nome = nome
        self.__vendas = []
        
    @property
    def NroCPF(self):
        return self.__nroCPF
    
    @property
    def Comissao(self):
        return self.__comissao
    
    
    def getDados(self):
        print(f"Nome{self.__nome} - Nro CPF:{self.__nroCPF}")
        pass
    
    def calculaRenda(self, pMes, pAno):
        vendas_mes_ano = [v for v in self._Vendedor__vendas if v.MesVenda == pMes and v.AnoVenda == pAno]
        total_vendas = sum(v.ValorVenda for v in vendas_mes_ano)
        renda = total_vendas * (self.__comissao/100)
        return renda
    
    


if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)

    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print(func.getDados())
        print("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))
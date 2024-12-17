#Emanuel Martins - 2022007043
#Programação Orientada a Objetos


from abc import ABC, abstractmethod

    
class PontoFunc:
    def __init__ (self,mes,ano,nroFaltas,nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos
        
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def nroFaltas(self):
        return self.__nroFaltas
    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    #Lança uma ausencia de aula e um dia de trabalho
    def lancaFaltas(self,nroFaltas):
        self.__nroFaltas = self.__nroFaltas + nroFaltas 
        return self.__nroFaltas
    
    #Lança o atraso, mas como?     
    def lancaAtrasos(self,nroAtrasos):
        self.__nroAtrasos += nroAtrasos
        self.__nroAtrasos

class Funcionario(ABC):
    def __init__ (self,codigo,nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    #Adiciona na Lista do Mes o PONTO
    def adicionaPonto(self,mes,ano,faltas,atrasos):
        return self.__pontoMensalFunc.append(PontoFunc(mes,ano,faltas,atrasos))
    
    #Como lançar falta? 
    def lancaFaltas(self,mes,ano,faltas):
        for i in self.__pontoMensalFunc:
            if i.mes == mes and  i.ano == ano:
               i.lancaFaltas(faltas)
        
    def lancaAtrasos(self,mes,ano,atrasos):    
        for i in self.pontoMensalFunc:
            if i.mes == mes and  i.ano == ano:
               i.lancaAtrasos(atrasos)
        
        
        
    def imprimeFolha(self,mes,ano):
       print(f"Codigo:{self.__codigo}")
       print(f"Nome:{self.__nome}")
       print(f"Salário líquido:{self.calculaSalario(mes,ano):.2f}")
       print(f"Bônus:{self.calculaBonus(mes,ano):.2f}")
       print("\n")
       pass 
       
    @abstractmethod
    def calculaSalario(self,mes,ano):
        pass
    
    @abstractmethod
    def calculaBonus(self,mes,ano):
        pass

        
class Professor(Funcionario):
    def __init__(self,codigo,nome,titulacao,salarioHora,nroHoras):
        super().__init__(codigo,nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroHoras = nroHoras
        
        
        
    @property
    def titulacao(self):
        return self.__titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora

    @property
    def NroAulas(self):
        return self.__nroHoras
    
    def calculaSalario(self, mes, ano):
        super().calculaSalario(mes, ano)
        nroFaltas = 0
        for i in self.pontoMensalFunc:
            if i.mes == mes and  i.ano == ano:
                nroFaltas = i.nroFaltas
        salario = self.__salarioHora * self.NroAulas - self.__salarioHora * nroFaltas
        return salario #Não tem que somar ao BONUS? 
    
    
    def calculaBonus(self, mes, ano):
        super().calculaBonus(mes, ano)
        bonus = 0
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                if(ponto.nroAtrasos<10):
                    percBonus = 10 - ponto.nroAtrasos
                    bonus = self.calculaSalario(mes,ano)*(percBonus/100)
        return bonus




class TecAdmin(Funcionario):
    def __init__(self, codigo, nome,funcao,salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal
        
    
    @property 
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    def calculaSalario(self, mes, ano):
        super().calculaSalario(mes, ano)
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and  ponto.ano == ano:
                  faltas = ponto.nroFaltas 
        salarioTec = self.__salarioMensal - (self.__salarioMensal/30)* faltas 
        return salarioTec      
    
    def calculaBonus(self, mes, ano):
        super().calculaBonus(mes, ano)
        bonus = 8 
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and  ponto.ano == ano:
                bonus -= 1
                
        v = (bonus/100)*self.calculaSalario(mes,ano)
        return v          


























if __name__ == "__main__":
 funcionarios = []
 prof = Professor(1, "Joao", "Doutor", 45.35, 32) 
 prof.adicionaPonto(4, 2021, 0, 0)
 prof.lancaFaltas(4, 2021, 2)
 prof.lancaAtrasos(4, 2021, 3)
 funcionarios.append(prof)
 tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
 tec.adicionaPonto(4, 2021, 0, 0)
 tec.lancaFaltas(4, 2021, 3)
 tec.lancaAtrasos(4, 2021, 4)
 funcionarios.append(tec)
 for func in funcionarios:
    func.imprimeFolha(4, 2021)
 print()

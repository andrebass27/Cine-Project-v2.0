'''Para descobrir linha onde o assento está:
        nº assento // nº colunas
    Para descobrir coluna onde o assento está:
        nº assento % nº colunas'''

class Assento:
    def __init__(self,numero,preço,disponivel=True):
        self.__numero = numero
        self.__preço = preço
        self.__disponivel = disponivel
    
    def getNumero(self):
        return self.__numero
    
    def getPreço(self):
        return self.__preço
    
    def getDisponivel(self):
        return self.__disponivel
    
    '''Antes de chamar este método, deve-se verificar
    o "status" do assento no momento'''
    def setDisponivel(self):
        self.__disponivel = not self.__disponivel
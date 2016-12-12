from assentos import Assento
import codecs

class GerenciadorAssentos:
    def __init__(self,matriz=[],listaAssentos=[], rendaCompra = 0,assentosDevolvidos = 0,nLinhas = 1,nColunas = 1,qtdOcupados=0):
        self.matriz = matriz
        self.__listaAssentos = listaAssentos
        self.__rendaCompra = rendaCompra
        self.__assentosDevol = assentosDevolvidos
        self.__nLinhas = nLinhas
        self.__nColunas = nColunas
        self.__qtdOcupados = qtdOcupados
    
    '''Método que retorna lista de assentos'''
    def getListaAssentos(self):
        return self.__listaAssentos
    
    '''Método que add assentos à lista de assentos
    É usado no método que faz a criação da matriz'''
    def setListaAssentos(self,elemento):
        self.__listaAssentos.append(elemento)
        
    '''Método que retorna a renda da compra'''
    def getRendaCompra(self):
        return self.__rendaCompra
    
    '''Método que soma preço de assentos comprados'''
    def setRendaCompra(self,valorCompra):
        self.__rendaCompra += valorCompra
    
    '''Método que retorna quantidade de assentos devolvidos'''
    def getAssentosDevol(self):
        return self.__assentosDevol
    
    '''Método que armazana a qtd de assentos devolvidos'''
    def setAssentosDevol(self,numAssentosDevolvidos):
        self.__assentosDevol += numAssentosDevolvidos
    
    '''Método que retorna nº de linhas'''
    def getNLinhas(self):
        return self.__nLinhas
    
    '''Método que retorna nº de colunas'''
    def getNColunas(self):
        return self.__nColunas
    
    '''Método que atribui nº de linhas'''
    def setNLinhas(self,nLinhas):
        self.__nLinhas = nLinhas
    
    '''Método que atribui nº de colunas'''
    def setNColunas(self,nColunas):
        self.__nColunas = nColunas
    
    '''Método que retorna qtd de assentos ocupados'''
    
    '''Método que retorna qtd de assentos ocupados'''
                
    '''função que cria uma matriz de objetos'''
    def criaMatriz(self):
        contador = 0
        [self.matriz.append([None]*self.getNColunas()) for i in range(self.getNLinhas())]
        
        for linha in range(self.getNLinhas()):
            for coluna in range(self.getNColunas()):
                novoAssento = Assento(contador,(valorAssento(contador//self.getNColunas())))
                self.matriz[linha][coluna] = novoAssento
                self.setListaAssentos(novoAssento)
                contador += 1
    
    '''Função que printa a matriz'''
    def printaMatriz(self):
        for i in range(self.getNLinhas()):
            for j in range(self.getNColunas()):
                if self.matriz[i][j].getDisponivel() == True:
                    print(str(self.matriz[i][j].getNumero()).rjust(qtdDigitos(self.getNLinhas(), self.getNColunas()),'0'),end=' ')
                else:
                    print('x'.rjust(qtdDigitos(self.getNLinhas(), self.getNColunas()),'x'),end=' ')
            print() 
        
    '''Método que verifica se há assentos digitados que já estão comprados'''
    def verificaDisponibilidade(self,listaNumeros):
        háAssentoJáComprado = False
        assentosJáComprados = []
        for numero in listaNumeros:
            for assento in self.getListaAssentos():
                if numero == assento.getNumero():
                    if assento.getDisponivel() == False:
                        assentosJáComprados.append(assento.getNumero())
                        háAssentoJáComprado = True
        if háAssentoJáComprado == False:
            return True
        else:
            for numAssento in assentosJáComprados:
                print("Assento %d já foi comprado." %numAssento)
    
    '''Método que verifica se todos os assentos estão comprados
    Para que seja feita a devolução'''
    def verificaDispDevol(self,listaNumeros):
        assentoComprado = True
        assentosNãoComprados = []
        for numero in listaNumeros:
            for assento in self.getListaAssentos():
                if numero == assento.getNumero():
                    if assento.getDisponivel() == True:
                        assentosNãoComprados.append(assento.getNumero())
                        assentoComprado = False
        if assentoComprado == True:
            return True
        else:
            for numAssento in assentosNãoComprados:
                print("Assento %d não foi comprado." %numAssento)
    
    
    '''Método para compra de assentos.
    listaAssentos possui os assentos já APTOS
    à serem comprados'''
    def comprarAssento(self,listaAssentosComp):
        for assento in listaAssentosComp:
            for assento2 in self.getListaAssentos():
                if assento == assento2.getNumero():
                    assento2.setDisponivel()
                    self.setRendaCompra(assento2.getPreço())
    
    
    '''Método para devolução de assentos.
    listaAssentosDev possui os assentos já APTOS
    à serem devolvidos'''
    def devolverAssento(self,listaAssentosDev):
        for assento in listaAssentosDev:
            for assento2 in self.getListaAssentos():
                if assento == assento2.getNumero():
                    assento2.setDisponivel()
                    self.setAssentosDevol(1)
                    '''Subtrai 90% do preço do assento devolvido na renda'''
                    self.setRendaCompra(assento2.getPreço()*(-0.9))
    
    
    '''Método que retornará a quantidade de
    assentos ocupados no momento.'''
    def assentosOcupados(self):
        assentosOcupados = 0
        for assento in self.getListaAssentos():
            if assento.getDisponivel() == False:
                assentosOcupados += 1
        return assentosOcupados
    
    '''Método que faz resumo da venda'''
    '''Fazer isso "manualmente" na interface'''
    '''Não é bom que métodos printem coisas'''
    def resumoVendas(self):
        self.printaMatriz()
        print('\nOcupação da sala no momento: %d' %(self.assentosOcupados()))
        print('Quantidade de ingressos devolvidos: %d' %(self.getAssentosDevol()))
        print('Valor total apurado: R$ %.2f' %(self.getRendaCompra()))
    
    '''Método para salvar dados no arquivo'''
    def salvaNoArquivo(self):
        '''Salva numa lista os assentos que estão ocupados.'''
        assentosOcupados = []
        [assentosOcupados.append(assento.getNumero()) for assento in self.getListaAssentos() if assento.getDisponivel()==False]
        arquivo = codecs.open('Sala Cinema.txt','w','latin-1')
        arquivo.write('Número de linhas:\r\n')
        arquivo.write('%d\r\n' %self.getNLinhas())
        arquivo.write('Número de colunas:\r\n')
        arquivo.write('%d\r\n' %self.getNColunas())
        arquivo.write("Assentos Ocupados:\r\n")
        for número in assentosOcupados:
            arquivo.write('%s - ' %número)
        arquivo.write('\r\n')
        arquivo.write('Qtd Assentos Ocupados:\r\n')
        arquivo.write('%d\r\n' %self.assentosOcupados())
        arquivo.write('Total Vendas:\r\n')
        arquivo.write('%.2f\r\n' %self.getRendaCompra())
        arquivo.write('Qtd Assentos Devolvidos:\r\n')
        arquivo.write('%d' %self.getAssentosDevol())
        arquivo.close()
        
    '''Método para ler informações do arquivo'''
    def lerArquivo(self):
        arquivo = open('Sala Cinema.txt','r')
        conteúdo = arquivo.readlines()
        
        '''Passa para o programa o número de linhas do programa anterior'''
        self.setNLinhas(int(conteúdo[1].replace('\n','')))
        '''Passa para o programa o número de colunas do programa anterior'''
        self.setNColunas(int(conteúdo[3].replace('\n','')))
        
        '''Para o programa rodar, é necessário que a matriz seja criada. Do contrário,
        a lista de assentos vai estar com apenas um assento (valor padrão),
        e consequentemente, não será possível ocupar os assentos'''
        #matriz criada com o número de linhas e colunas lidos do arquivo
        self.criaMatriz()
        
        '''Passa para o programa os assentos que estavam ocupados no programa anterior'''
        #Cria uma lista com cada assento separado
        assentosSeparados = conteúdo[5].replace('\n','').split(' - ')
        for numAssento in assentosSeparados[:-1]:
            for assento2 in self.getListaAssentos():
                if int(numAssento) == assento2.getNumero():
                    assento2.setDisponivel()
        '''Edita quantidade de assentos ocupados'''
        #qtdAssentosOcupados = len(assentosSeparados[:-1])
        #self.setQtdOcupados(qtdAssentosOcupados)
        '''Passa para o programa a renda da compra do outro programa'''
        self.setRendaCompra(float(conteúdo[9].replace('\n','')))
        '''Passa para o programa a quantidade de assentos devolvidos anteriormente'''
        self.setAssentosDevol(int(conteúdo[11].replace('\n','')))
'''*******************************************FUNÇÕES**************************************************'''

'''FUNÇÃO RECURSIVA que determina valor do assento'''
'''A linha à qual o assento pertence, pode ser determinada
por nºdoAssento // nºColunas'''
def valorAssento(linhaAssento):
    #caso base
    if linhaAssento == 0:
        return 20
    else:
        return valorAssento(linhaAssento-1) - 1

'''FUNÇÃO que descobre quantidade de dígitos'''
def qtdDigitos(qtdLinhas,qtdColunas):
    return len(str(qtdLinhas*qtdColunas-1))

'''Função que verifica assentos maiores que o máximo
permitido ou menores que o mínimo permitido'''
'''Caso seja válido, retorna True'''
def verificaMaxMin(listaAssentos,linhas,colunas):
    if max(listaAssentos) > (linhas*colunas)-1 or min(listaAssentos) < 0:
        return False
    else:
        return True
'''Função que verifica se há assentos repetidos'''
def verificaRepetição(listaAssentos):
    existeRepetido = False
    for numero in listaAssentos:
        if listaAssentos.count(numero)>1:
            existeRepetido = True
    if existeRepetido == False:
        return True
    else:
        return False
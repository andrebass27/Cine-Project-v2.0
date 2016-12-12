from gerenciadorAssentos import *

'''Criação da sala de cinema'''
while True:
    cinema = GerenciadorAssentos()
    try:
        cinema.lerArquivo()
        break
        
        '''Caso haja erro de índice'''
    except(IndexError):
        try:
            linhas = int(input("Informe o número de fileiras da sala: "))
            #Verifica se linhas recebe valor válido (acima de 0)
            if linhas <= 0 or linhas > 20:
                print("VALOR INVÁLIDO. DIGITE VALORES MAIORES QUE 0 E MENORES QUE 21.\n")
                continue
            cinema.setNLinhas(linhas)
            colunas = int(input("Informe o número de colunas da sala: "))
            #Verifica se colunas recebe valor válido(acima de 0)
            if colunas <= 0:
                print("VALOR INVÁLIDO. DIGITE VALORES MAIORES QUE 0.\n")
                continue
            cinema.setNColunas(colunas)
            print()
            cinema.criaMatriz()
            cinema.printaMatriz()
            break
        #except não permite que usuário digite letras
        except(ValueError):
            print("\nDIGITE SOMENTE NÚMEROS.\n")
    
            '''Caso arquivo não seja encontrado, programa criará um'''
    except(FileNotFoundError):
        abrirArquivo = open('Sala Cinema.txt','w')
        abrirArquivo.close()
        continue

'''Menu de Opções'''
while True:
    print()
    print("***********************************************")
    print("Bem vindo ao sistema de venda de ingressos.".upper())
    print("Escolha a operação:")
    print("1 - Comprar ingressos")
    print("2 - Devolver ingressos")
    print("3 - Resumo das vendas")
    print("4 - Sair")
    print("***********************************************")
    try:
        escolha = int(input("Digite sua escolha: "))
    #except não permite que usuário digite letras
    except(ValueError):
        print("DIGITE APENAS NÚMEROS.")
        continue
    
    '''Verifica se escolha recebeu valores válidos'''
    if escolha < 1 or escolha > 4:
        print("Escolha de 1 a 4.")
        continue
    print()
    
    '''Determina o que acontece com cada escolha'''
    '''Condição para o programa encerrar'''
    if escolha == 4:
        #Salva no arquivo e encerra sessão
        cinema.salvaNoArquivo()
        print("SESSÃO ENCERRADA!")
        break
    
        '''Condição para o programa entrar em compra de ingressos'''
    elif escolha == 1:
        listaVerificação = []
        #imprime matriz antes de pedir assentos para compra
        cinema.printaMatriz()
        print()

        assentosCompra = input('Qual(is) assento(s) deseja comprar? ')
        assentosLista = assentosCompra.split(',')
        
        try:
            for numAssento in assentosLista:
                listaVerificação.append(int(numAssento))
        except(ValueError):
            print("Digitou caractere(s). Digite apenas números.")
            continue
        
            '''Verifica se assentos estão na sala de cinema'''
        if verificaMaxMin(listaVerificação, cinema.getNLinhas(), cinema.getNColunas()):
            '''Verifica se há assentos digitados mais de uma vez'''
            if verificaRepetição(listaVerificação):
                '''Verifica se o assento está disponível para compra'''
                if cinema.verificaDisponibilidade(listaVerificação):
                    '''Se tudo estiver correto, assentos são comprados'''
                    cinema.comprarAssento(listaVerificação)
                    print()
                    cinema.printaMatriz()
            else:
                print("Foram digitados assentos repetidos.")
                continue
        else:
            print("Assentos não existem!")
            continue
    
        '''Condição para programa entrar em devolução de ingressos'''
    elif escolha == 2:
        listaVerificação = []
        #imprime matriz antes de pedir assentos para devolução
        cinema.printaMatriz()
        print()
        
        assentosDevol = input('Qual(is) assento(s) deseja devolver? ')
        assentosDevolLista = assentosDevol.split(',')
        
        '''Converte para inteiro e salva na lista de verificação'''
        try:
            for numAssento in assentosDevolLista:
                listaVerificação.append(int(numAssento))
        except(ValueError):
            print("Digitou letra. Digite números.")
            continue
        
        '''Verifica se assentos estão na sala de cinema'''
        if verificaMaxMin(listaVerificação, cinema.getNLinhas(), cinema.getNColunas()):
            '''Verifica se há assentos digitados mais de uma vez'''
            if verificaRepetição(listaVerificação):
                '''Verifica se os assentos foram comprados'''
                if cinema.verificaDispDevol(listaVerificação):
                    '''Se tudo estiver ok, assentos são devolvidos'''
                    cinema.devolverAssento(listaVerificação)
                    print()
                    cinema.printaMatriz()
            else:
                print("Foram digitados assentos repetidos.")
        else:
            print("Assentos não existem")
    
    
        '''Condição para programa entrar em resumo das vendas'''
    elif escolha == 3:
        cinema.resumoVendas()
    
    
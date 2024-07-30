import os

def menu(primeira_vez):

    # Declaração de váriaveis locais:
    continuar_repetindo = True
    opcao_invalida = False

    while continuar_repetindo == True:

        # "If statement" que irá exibir o menu pela primeira vez após o usuário iniciar o programa:
        if primeira_vez == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Bem vindo ao Banco Grande ::..\n')
            print('Você ainda não possui uma conta.')
            print('\n1 - Abrir conta')
            print('6 - Sair\n')
            if opcao_invalida == True:
                print('obs: Digite uma opção válida.')
            opcao = input('Digite a opção desejada: ')
            if opcao == '1' or opcao == '6':
                return int(opcao)
            else:
                opcao_invalida = True

        # "If statement" que irá exibir o menu após o usuário ter aberto a conta:
        elif primeira_vez == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Bem vindo ao Banco Grande ::..\n')
            print('2 - Realizar depósito')
            print('3 - Realizar saque')
            print('4 - Simular empréstimos')
            print('5 - Extrato')
            print('6 - Sair\n')
            if opcao_invalida == True:
                print('obs: Digite uma opção válida.')
            opcao = input('Digite a opção desejada: ')
            if opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5' or opcao == '6':
                return int(opcao)
            else:
                opcao_invalida = True



def abrir_conta():

    # Declaração de váriaveis locais:
    continuar_repetindo = True
    nome_ou_saldo_invalido = False

    # "While loop" que começa o loop para o usuário abrir a conta:
    while continuar_repetindo == True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Bem vindo ao Banco Grande ::..\n')
            print('Informe os seus dados para começarmos o seu cadastro (pressione "Enter" 2 vezes para sair): ')
            if nome_ou_saldo_invalido == True:
                print('obs: Digite um nome e um saldo válido e sem símbolos')
            nome = input('\nInforme o seu nome: ')
            saldo_inicial = input('Informe o seu saldo: ')
            if nome == '' and saldo_inicial == '':
                return 6
            saldo_inicial = float(saldo_inicial)
            if nome >= 'A' and nome <= 'z' and saldo_inicial >= 0:
                return nome, saldo_inicial
            else:
                nome_ou_saldo_invalido = True
        except:
                nome_ou_saldo_invalido = True



def realizar_deposito(saldo):  

    # Declaração de váriaveis locais:
    valor_invalido = False

    # "While loop" que começa o loop para o usuário realizar o depósito:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Bem-vindo a área de depósito ::..\n')
        if valor_invalido == True:
            print("Obs: Digite um valor válido.")
        deposito = input('Insira o valor que deseja depositar em sua conta (digite 0 para cancelar): ')
        if deposito == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Operação cancelada! ::..\n')
            input('Pressione "Enter" para voltar ao menu principal: ')
            return int(deposito)
        
        # "Try e if statements" que irão verificar se o que o usuário escreveu é um número positivo:
        try:
            deposito = float(deposito)
            if deposito > 0:
                saldo += deposito
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n..:: Depósito realizado com sucesso ::..\n')
                print(f'Seu deposito no valor de R$ {deposito:.2f} foi realizado com sucesso.')
                print(f'Seu saldo atual na conta e de R$ {saldo:.2f}\n')
                input('Pressione "Enter" para voltar ao menu principal: ')
                return(deposito)
            else: 
                valor_invalido = True
        except:
            valor_invalido = True



def realizar_saque(saldo):
    
    # Declaração de váriaveis locais:
    valor_invalido = False

    # "While loop" que começa o loop para o usuário realizar o depósito:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Bem-vindo a área de saques ::..\n')
        if valor_invalido == True:
            print("Obs: Digite um valor válido e compativel com o saldo atual da conta.")
        valor_do_saque = input('Insira o valor que deseja sacar de sua conta (digite 0 para cancelar): ')
        if valor_do_saque == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Operação cancelada! ::..\n')
            input('Pressione "Enter" para voltar ao menu principal: ')
            return int(valor_do_saque) 

        # "Try e if statements" que irão verificar se o que o usuário escreveu é um número positivo,
        #  se é um valor menor que o do saldo do usuário e se da pra ser sacado somente com notas:           
        try:
            valor_do_saque = float(valor_do_saque)
            if valor_do_saque <= saldo and valor_do_saque >= 0: 
                divisao_200 = valor_do_saque
                notas_de_200 = int(divisao_200 / 200)
                divisao_100 = divisao_200 % 200
                notas_de_100 = int(divisao_100 / 100)
                divisao_50 = divisao_100 % 100
                notas_de_50 = int(divisao_50 / 50)
                divisao_20 = divisao_50 % 50
                notas_de_20 = int(divisao_20 / 20)
                divisao_10 = divisao_20 % 20
                notas_de_10 = int(divisao_10 / 10)
                divisao_5 = divisao_10 % 10
                notas_de_5 = int(divisao_5 / 5)
                divisao_2 = divisao_5 % 5
                notas_de_2 = int(divisao_2 / 2)
                divisao_moedas = divisao_2 % 2
                if divisao_moedas == 0:
                    saldo -= valor_do_saque
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\n..:: Saque realizado com sucesso ::..\n')
                    print('Notas a serem retiradas:')
                    if notas_de_200 != 0:
                        print(f'{notas_de_200} notas de R$ 200.00')
                    if notas_de_100 != 0:
                        print(f'{notas_de_100} notas de R$ 100.00')
                    if notas_de_50 != 0:
                        print(f'{notas_de_50} notas de R$ 50.00')
                    if notas_de_20 != 0:
                        print(f'{notas_de_20} notas de R$ 20.00')
                    if notas_de_10 != 0:
                        print(f'{notas_de_10} notas de R$ 10.00')
                    if notas_de_5 != 0:
                        print(f'{notas_de_5} notas de R$ 5.00')
                    if notas_de_2 != 0:
                        print(f'{notas_de_2} notas de R$ 2.00')
                    print(f'\nSeu saque no valor de R$ {valor_do_saque:.2f} foi realizado com sucesso.')
                    print(f'Seu saldo atual na conta é de R$ {saldo:.2f}')
                    input('\nPressione "Enter" para voltar ao menu principal: ')
                    return valor_do_saque                    
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\n..:: Não é possivel sacar o valor informado ::..\n')
                    print('O caixa eletrônico possui somente notas.')
                    print('Por isso informe um valor que de para ser sacado somente com notas.')
                    input('\nPressione "Enter" para voltar ao menu principal: ')
                    return 0
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n..:: Saldo insuficiente! ::..\n')
                input('Pressione "Enter" para voltar ao menu principal: ')
                return 0
        except:
            valor_invalido = True



def simular_emprestimo(saldo):
    
    # Declaração de váriaveis locais:
    valor_invalido_1 = False
    valor_invalido_2 = False
    opcao_invalida = False

    # "While loop" que começa o loop para o usuário realizar a simulação de empréstimo:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Bem-vindo a área de empréstimos ::..\n')
        if valor_invalido_1 == True:
            print("Obs: Digite um valor válido.")
        valor = input('Insira o valor que você deseja fazer o empréstimo (digite 0 para cancelar): ')
        if valor == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Operação cancelada! ::..\n')
            input('Pressione "Enter" para voltar ao menu principal: ')
            return int(valor)
        
        # "Try e if statements" que irão verificar se o que o usuário escreveu é um número positivo:
        try:
            valor = float(valor)
            if valor > 0:
                break
            else:
                valor_invalido_1 = True  
        except:
            valor_invalido_1 = True

    # "While loop" que pergunta ao usuário de quantos meses é o emprestimo:    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Bem-vindo a área de empréstimos ::..\n')
        print('A taxa fixa é de 2% ao mês.\n')
        if valor_invalido_2 == True:
            print("Obs: Digite um valor válido.")
        meses = input('Digite em quantos meses deseja pagar o empréstimo (1-24 meses): ')
        if meses == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Operação cancelada! ::..\n')
            input('Pressione "Enter" para voltar ao menu principal: ')
            return int(valor)
        # "Try e if statements" que irão verificar se o que o usuário escreveu é um número dentro das quantidades de meses ofertadas:
        try:
            meses = int(meses)
            if meses >= 1 and meses <= 24:
                break
            else:
                valor_invalido_2 = True
        except:
            valor_invalido_2 = True

    # "While loop" que mostra os dados do empréstimo e que pergunta se o usuário vai querer realizar o empréstimo:
    while True:    
        os.system('cls' if os.name == 'nt' else 'clear')
        juros = valor *  0.02 * meses
        total = valor + juros
        taxa_mensal = total / meses
        print('\n..:: Dados da simulação do empréstimo ::..\n')
        print('Assim ficou a sua simulação de empréstimo:')
        print(f'Valor do empréstimo: {valor:.2f} R$')
        print('Taxa de juros: 2% ao mês')
        print(f'Meses a pagar: {meses} meses')
        print(f'Juros: {juros:.2f} R$')
        print(f'Taxa mensal: {taxa_mensal:.2f} R$')
        print(f'\nTotal a ser pago: {total:.2f} R$')
        print('\n1 - Realizar o empréstimo na minha conta')
        print('2 - Voltar ao menu principal\n')
        if opcao_invalida == True:
            print("Obs: Digite uma opção válida.")
        opcao = input('Selecione a opção desejada: ')

        # "if statements" que irão verificar o que o usuário escreveu e redirecionar para o caminho certo:
        if opcao == '1':
            saldo += valor
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Empréstimo realizado com sucesso ::..\n')
            print(f'Seu empréstimo no valor de R$ {valor:.2f} foi realizado com sucesso.')
            print(f'Seu saldo atual na conta e de R$ {saldo:.2f}\n')
            input('Pressione "Enter" para voltar ao menu principal: ')
            return valor, juros
        elif opcao == '2':
            return 0
        else:
            opcao_invalida = True



def extrato(nome, saldo_inicial, saldo, quantidade_de_depositos, valor_total_dos_depositos, quantidade_de_saques, valor_total_dos_saques, valor_total_dos_juros):
    
    # Comandos que vão mostrar todos os dados do extrato:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Extrato ::..\n')
    print(f'Nome: {nome}')
    print(f'Saldo inicial: R$ {saldo_inicial:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}')
    print(f'Foram feitos no total {quantidade_de_depositos} depósitos.')
    print(f'Valor total dos depósitos realizados: R$ {valor_total_dos_depositos:.2f}')
    print(f'Foram feitos no total {quantidade_de_saques} saques.')
    print(f'Valor total dos saques realizados: R$ {valor_total_dos_saques:.2f}')
    print(f'Valor total dos juros recebidos: R$ {valor_total_dos_juros:.2f}')
    input('\nPara retornar ao menu pressione "Enter": ')



def sair():

    # Comandos que vão mostrar a mensagem final antes do programa finalizar:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Obrigado por usar os serviços do Banco Grande ::..\n')
    input('Pressione "Enter" para finalizar o programa: ')
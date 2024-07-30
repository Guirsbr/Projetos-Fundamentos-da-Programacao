import os
import string
import csv

def num_para_letra(x):
    letras = list(string.ascii_uppercase)
    contador = 0
    try:
        if x.isdecimal():
            for y in letras:
                if x == str(contador):
                    x = y
                    return x
                contador += 1
    except:
        x = str(x)
        if x.isdecimal():
            for y in letras:
                if x == str(contador):
                    x = y
                    return x
                contador += 1
    if x >= 'A' and x <= 'Z':
        for y in letras:
            if x == y:
                x = contador
                return x
            contador += 1


def menu(primeira_vez):

    opcao_invalida = False
    numero_linhas_invalido = False

    while True:

        if primeira_vez == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Bem vindo ao Cine +Arte Tanópolis ::..\n')
            if opcao_invalida == True:
                print('obs: Digite somente valores e números.')
            if numero_linhas_invalido == True:
                print('obs: O número de fileiras informado excede a quantidade de letras disponíveis.')
            try:
                valor_ingresso = float(input('Digite o valor do ingresso em Reais: '))
                fileira_linhas = int(input('Digite a quantidade de fileiras que o cinema comporta: '))
                assentos_colunas = int(input('Digite a quantidade de assentos por fileiras que o cinema comporta: '))
                opcao_invalida = True
                letras = list(string.ascii_uppercase)  # Lista de letras de A a Z
                if fileira_linhas <= len(letras):
                    M = []
                    for x in range(fileira_linhas):
                        M.append([0] * assentos_colunas)
                    for x in range(fileira_linhas):
                        for y in range(assentos_colunas):
                            M[x][y] = {'reservado': '.', 'categoria': '', 'idade': ''}  
                    return valor_ingresso, M   
                else:
                    numero_linhas_invalido = True
                    opcao_invalida = False 
            except:
                opcao_invalida = True 
                numero_linhas_invalido = False              

        if primeira_vez == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Bem vindo ao Cine +Arte Tanópolis ::..\n')
            print('1 - Carregar Dados')
            print('2 - Consultar Situação de um Assento')
            print('3 - Fazer Reservas de “n” Assentos')
            print('4 - Liberar Reserva de “n” Assentos')
            print('5 - Visualizar Mapa do Cinema')
            print('6 - Relatórios')
            print('7 - Salvar Dados')
            print('8 - Sair\n')
            if opcao_invalida == True:
                print('obs: Digite uma opção válida.')
            opcao = input('Digite a opção desejada: ')
            V = ('1', '2', '3', '4', '5', '6', '7', '8')
            if opcao in V:
                return int(opcao)
            else:
                opcao_invalida = True


def carregar_dados(matriz):

    arquivo_invalido = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Carregar Dados ::..\n')
        try:
            if arquivo_invalido == True:
                print('Obs: O arquivo digitado não existe.\n')
            print('Para voltar ao menu pressione a tecla Enter.')
            arquivo = input('Digite o nome do arquivo com o registro das reservas: ')
            if arquivo == '':
                return matriz
            arquivo = open(arquivo)
            reader = csv.reader(arquivo)
            reservas = list(reader)
            arquivo.close()
            indice = reservas.pop(0)
            break
        except:
            arquivo_invalido = True

    alfabeto = list(string.ascii_uppercase)
    for x in range(len(reservas)):
        contador = 0
        assento = reservas[x][0]

        for y in alfabeto:
            if y == assento[0]:
                linha = contador
                break
            contador += 1
        assento = assento.replace(assento[0], '')
        coluna = int(assento) - 1
        try:
            matriz[linha][coluna]['reservado'] = 'X'
            matriz[linha][coluna]['categoria'] = reservas[x][1]
            matriz[linha][coluna]['idade'] = reservas[x][2]
        except:
            continue

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Carregar Dados ::..\n')
    print('Dados carregados com sucesso!\n')
    input('Pressione Enter para voltar ao menu: ')
    return matriz


def consultar_assento(matriz, valor_ingresso):

    opcao_invalida = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Consultar Assento ::..\n')
        if opcao_invalida == True:
            print('obs: Digite um assento válido.')
        X = input('Digite o assento que deseja verificar: ')
        
        try:
            linha_1 = X[0]
            linha_2 = X[0]
            X = X.replace(linha_1, '')
            coluna_1 = int(X) - 1

            if linha_1 >= 'A' and linha_1 <= 'Z':
                letras = list(string.ascii_uppercase)        
                contador = 0

                for x in letras:
                    if x == linha_1:
                        linha_1 = contador
                        break
                    contador += 1
                
                assento = matriz[linha_1][coluna_1]
                if assento['reservado'] == '.':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\n..:: Consultar Assento ::..\n')
                    print(f'O assento {linha_2}{coluna_1 + 1} está livre.\n')
                    input('Pressione Enter para voltar ao menu: ')
                    return
                elif assento['reservado'] == 'X':
                    categoria = assento['categoria']
                    idade = assento['idade']
                    if not(idade >= '18' and idade <= '59'):
                        valor_ingresso = valor_ingresso / 2
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\n..:: Consultar Assento ::..\n')
                    print(f'O assento {linha_2}{coluna_1 + 1} está reservado.')
                    print(f'O valor pago pelo assento é de: R$ {valor_ingresso:.2f}')
                    print(f'A categoria do ocupante é: {categoria}')
                    print(f'A idade do ocupante é: {idade}\n')
                    input('Pressione Enter para voltar ao menu: ')
                    return
            else:
                opcao_invalida = True
        except:
            opcao_invalida = True   


def reservar_assento(matriz):

    opcao_invalida = False
    assento_informado_ocupado = False
    categoria_idade_invalida = False

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Reservação de Assentos ::..\n')
            if opcao_invalida == True:
                print('Obs: Digite fileiras e assentos válidos.')
            if assento_informado_ocupado == True:
                print('Obs: Informe somente assentos que estejam livres.')
            fileira_linha = input("Digite a fileira (letra) dos assentos a serem reservados: ")
            if len(fileira_linha) == 1 and fileira_linha >= 'A' and fileira_linha <= 'Z':
                fileira = num_para_letra(fileira_linha)
                if fileira < len(matriz):

                    assentos_coluna = input('Digite o número dos assentos a serem reservados separados por ",": ')
                    assentos_coluna = assentos_coluna.replace(' ', '')
                    assentos_coluna = assentos_coluna.split(',')
                    contador = 0
                    for x in assentos_coluna:
                        assentos_coluna[contador] = int(x) - 1
                        contador += 1

                    assento_informado_ocupado = False
                    for x in assentos_coluna:
                        if matriz[fileira][x]['reservado'] == 'X':
                            assento_informado_ocupado = True
                            opcao_invalida = False
                            break

                    if assento_informado_ocupado == False:
                        for x in assentos_coluna:
                            while True:
                                try:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('\n..:: Reservação de Assentos ::..\n')
                                    if categoria_idade_invalida == True:
                                        print('Obs: Categoria ou idade digitados são inválidos.')
                                    categoria = input(f'Digite a categoria do ocupante do assento {x + 1}: ')
                                    idade = input(f'Digite a idade do ocupante do assento {x + 1}: ')
                                    categorias = ['MM', 'I', 'MI'] 
                                    if categoria in categorias and int(idade) >= 0:
                                        matriz[fileira][x]['reservado'] = 'X'
                                        matriz[fileira][x]['categoria'] = categoria
                                        matriz[fileira][x]['idade'] = idade
                                        categoria_idade_invalida = False
                                        break
                                    else:
                                        categoria_idade_invalida = True
                                except:
                                    categoria_idade_invalida = True

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('\n..:: Reservação de Assentos ::..\n')
                        print('Assento(s) reservado(s) com sucesso.')
                        input('\nDigite enter para voltar ao menu: ')
                        return matriz

                else:
                    opcao_invalida = True
                    assento_informado_ocupado = False
            else:
                opcao_invalida = True
                assento_informado_ocupado = False
        except:
            opcao_invalida = True
            assento_informado_ocupado = False


def liberar_assento(matriz):

    opcao_invalida = False
    assento_informado_livre = False

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Liberação de Assentos ::..\n')
            if opcao_invalida == True:
                print('Obs: Digite fileiras e assentos válidos.')
            if assento_informado_livre == True:
                print('Obs: Informe somente assentos que estejam ocupados.')
            fileira_linha = input("Digite a fileira (letra) dos assentos a serem liberados: ")
            if len(fileira_linha) == 1 and fileira_linha >= 'A' and fileira_linha <= 'Z':
                fileira = num_para_letra(fileira_linha)
                if fileira < len(matriz):

                    assentos_coluna = input('Digite o número dos assentos a serem liberados separados por ",": ')
                    assentos_coluna = assentos_coluna.replace(' ', '')
                    assentos_coluna = assentos_coluna.split(',')
                    contador = 0
                    for x in assentos_coluna:
                        assentos_coluna[contador] = int(x) - 1
                        contador += 1

                    for x in assentos_coluna:
                        if matriz[fileira][x]['reservado'] == '.':
                            assento_informado_livre = True
                            opcao_invalida = False
                            break
                        if matriz[fileira][x]['reservado'] == 'X':
                            matriz[fileira][x]['reservado'] = '.'
                            matriz[fileira][x]['categoria'] = ''
                            matriz[fileira][x]['idade'] = ''
                            assento_informado_livre = False

                    if assento_informado_livre == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('\n..:: Liberação de Assentos ::..\n')
                        print('Assento(s) liberado(s) com sucesso.')
                        input('\nDigite enter para voltar ao menu: ')
                        return matriz
            
                else:
                    opcao_invalida = True
                    assento_informado_livre = False
            else:
                opcao_invalida = True
                assento_informado_livre = False
        except:
            opcao_invalida = True
            assento_informado_livre = False


def mapa_cinema(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Mapa do Cinema ::..\n')

    print('   ', end='')
    for i in range(1, len(matriz[0]) + 1):
        print(str(i).center(3), end=' ')
    print()

    for i, linha in enumerate(matriz):
        print(chr(65 + i), end='  ')
        for assento in linha:
            if assento['reservado'] == '.':
                print('·'.center(3), end=' ')
            else:
                print('X'.center(3), end=' ')
        print()

    print('\nEste é o mapa do cinema.\n')
    input('Pressione Enter para voltar ao menu: ')
    return


def relatorios(matriz, valor):

    opcao_invalida = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Relatórios ::..\n')
        print('1 - Tabela com as informações das reservas.')
        print('2 - Quantidade de assentos liberados e vagos.')
        print('3 - Lista com as informações financeiras.')
        print('4 - Voltar ao menu.\n')
        if opcao_invalida == True:
            print('obs: Digite uma opção válida.')
        opcao = input('Digite a opção desejada: ')
        match opcao:
            case '1':

                contador_linha = 0

                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n..:: Relatórios ::..\n')
                print(' Assento | Categoria | Idade ')
                for x in matriz:
                    contador_coluna = 0

                    for y in x:
                        if y['reservado'] == 'X':
                            linha = num_para_letra(contador_linha)
                            categoria = y['categoria']
                            idade = y['idade']
                            if contador_coluna + 1 >= 10 and len(categoria) == 2:
                                print(f'    {linha}{contador_coluna + 1}  |     {categoria}    |   {idade}')
                            elif contador_coluna + 1 >= 10:
                                print(f'    {linha}{contador_coluna + 1}  |    {categoria}       | {idade}')
                            elif len(categoria) == 2:
                                print(f'    {linha}{contador_coluna + 1}   |     {categoria}    |   {idade}')
                            else:
                                print(f'    {linha}{contador_coluna + 1}   |     {categoria}     |   {idade}')
                        
                        contador_coluna += 1
                    
                    contador_linha += 1
                
                input('\n Pressine Enter para voltar: ')
                
            case '2':

                quantidade_de_assentos = (len(matriz) * len(matriz[0]))
                assentos_liberados = 0
                assentos_ocupados = 0
                for x in matriz:
                    for y in x:
                        if y['reservado'] == '.':
                            assentos_liberados += 1
                        elif y['reservado'] == 'X':
                            assentos_ocupados += 1

                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n..:: Relatórios ::..\n')
                print(f'A quantidade total de assentos é: {quantidade_de_assentos}')
                print(f'A quantidade assentos liberados é: {assentos_liberados}')
                print(f'A quantidade assentos ocupados é: {assentos_ocupados}')
                input('\n Pressine Enter para voltar: ')

            case '3':
                meia_menor = 0
                inteira = 0
                meia_idoso = 0
                total = 0
                for x in matriz:
                    for y in x:
                        if y['reservado'] == 'X':
                            if int(y['idade']) >= 0 and int(y['idade']) <= 17:
                                meia_menor += 1
                                total += 1
                            if int(y['idade']) >= 18 and int(y['idade']) <= 59:
                                inteira += 1
                                total += 1
                            if int(y['idade']) >= 60:
                                meia_idoso += 1
                                total += 1

                porcentagem_meia_menor = (meia_menor / total) * 100
                porcentagem_inteira = (inteira / total) * 100
                porcentagem_meia_idoso = (meia_idoso / total) * 100
                valor_meia_menor = (valor / 2) * meia_menor
                valor_inteira = valor * inteira
                valor_meia_idoso = (valor / 2) * meia_idoso
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n..:: Relatórios ::..\n')
                if meia_menor >= 10:
                    print(f'Meia menor:   {meia_menor}  -   {porcentagem_meia_menor:.1f} %   -   R$ {valor_meia_menor:.2f}')
                else:
                    print(f'Meia menor:   {meia_menor}   -   {porcentagem_meia_menor:.1f} %   -   R$ {valor_meia_menor:.2f}')
                if inteira >= 10:
                    print(f'Inteira:      {inteira}  -   {porcentagem_inteira:.1f} %   -   R$ {valor_inteira:.2f}')
                else:
                    print(f'Inteira:      {inteira}   -   {porcentagem_inteira:.1f} %   -   R$ {valor_inteira:.2f}')
                if meia_idoso >= 10:
                    print(f'Meia idoso:   {meia_idoso}  -   {porcentagem_meia_idoso:.1f} %   -   R$ {valor_meia_idoso:.2f}')
                else:
                    print(f'Meia idoso:   {meia_idoso}   -   {porcentagem_meia_idoso:.1f} %   -   R$ {valor_meia_idoso:.2f}')
                if total >= 10:
                    print(f'Total:        {total}  -   100.0 %  -   R$ {valor_meia_menor + valor_inteira + valor_meia_idoso:.2f}')
                else:
                    print(f'Total:        {total}   -   100.0 %  -   R$ {valor_meia_menor + valor_inteira + valor_meia_idoso:.2f}')
                input('\nPressine Enter para voltar: ')
        
            case '4':
                return
            case _:
                opcao_invalida = True


def salvar(matriz):  

    arquivo_invalido = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n..:: Salvar Dados ::..\n') 
        if arquivo_invalido == True:
            print('Obs: Digite um arquivo válido.')
        nome_arquivo = input('Informe o nome do arquivo CSV para salvar as informações: ')
        
        if nome_arquivo == 'cinema.csv':
                
            with open(nome_arquivo, 'w', newline='') as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerow(['Assento', 'Categoria', 'Idade'])
                
                for i, fileira in enumerate(matriz):
                    fileira_letra = chr(i + 65)
                    for j, assento in enumerate(fileira):
                        if assento['reservado'] == 'X':
                            poltrona = f'{fileira_letra}{j + 1}'
                            categoria = assento['categoria']
                            idade = assento['idade']
                            writer.writerow([poltrona, categoria, idade])

            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n..:: Salvar Dados ::..\n') 
            print(f'As informações foram salvas em {nome_arquivo}.')
            input('\nDigite Enter para continuar')
            return
        
        else:
            arquivo_invalido = True


def sair():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Obrigado por usar os serviços do Cine +Arte Tanópolis ::..\n')
    input('Pressione "Enter" para finalizar o programa: ')

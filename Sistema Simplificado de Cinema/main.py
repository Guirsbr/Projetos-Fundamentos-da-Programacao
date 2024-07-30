import funcoes

# Declaração de váriaveis:
opcao = 0
primeira_vez = True


# "While loop" que chama as funções e altera as variáveis:

while True:

    if primeira_vez == True:
        V = funcoes.menu(primeira_vez)
        valor_ingresso = V[0]
        matriz = V[1]
        primeira_vez = False
    else:
        opcao = funcoes.menu(primeira_vez)     
        match opcao:
            case 1:
                matriz = funcoes.carregar_dados(matriz)
            case 2:
                funcoes.consultar_assento(matriz, valor_ingresso)
            case 3:
                matriz = funcoes.reservar_assento(matriz)
            case 4:
                matriz = funcoes.liberar_assento(matriz)
            case 5:
                funcoes.mapa_cinema(matriz)
            case 6:
                funcoes.relatorios(matriz, valor_ingresso)
            case 7:
                funcoes.salvar(matriz)
            case 8:
                funcoes.sair()
                break



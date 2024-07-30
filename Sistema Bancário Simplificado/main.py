import funcoes

# Declaração de váriaveis:
opcao = 0
primeira_vez = True
quantidade_de_depositos = 0
valor_total_dos_depositos = 0.0
quantidade_de_saques = 0
valor_total_dos_saques = 0.0
valor_total_dos_juros = 0.0

# "While loop" que chama as funções e altera as variáveis:

while opcao != 6:

    opcao = funcoes.menu(primeira_vez)
    if primeira_vez == True:
        primeira_vez = False

    if opcao == 1:
        nome_e_saldo_inicial = funcoes.abrir_conta()
        if nome_e_saldo_inicial == 6:
            opcao = 6
        else:
            nome, saldo_inicial = nome_e_saldo_inicial
            saldo_inicial = float(saldo_inicial)
            saldo = saldo_inicial

    if opcao == 2:
        valor_do_deposito = funcoes.realizar_deposito(saldo)
        if valor_do_deposito != 0:
            valor_total_dos_depositos += valor_do_deposito
            quantidade_de_depositos += 1
            saldo += valor_do_deposito

    if opcao == 3:
        valor_do_saque = funcoes.realizar_saque(saldo)
        if valor_do_saque != 0:
            valor_total_dos_saques += valor_do_saque
            quantidade_de_saques += 1
            saldo -= valor_do_saque

    if opcao == 4:
        simulacao_de_emprestimo = funcoes.simular_emprestimo(saldo)
        if simulacao_de_emprestimo != 0:
            valor_do_emprestimo, valor_dos_juros = simulacao_de_emprestimo
            valor_total_dos_juros += valor_dos_juros
            saldo += valor_do_emprestimo

    if opcao == 5:
        funcoes.extrato(nome, saldo_inicial, saldo, quantidade_de_depositos, valor_total_dos_depositos, quantidade_de_saques, valor_total_dos_saques, valor_total_dos_juros)

    if opcao == 6:
        funcoes.sair()



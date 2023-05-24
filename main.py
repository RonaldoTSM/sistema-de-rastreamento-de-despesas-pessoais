from modulo import*

while True:
    opcao = input('''
Sistema de Rastreamento de Despesas Pessoais
[A]: Adicionar transação
[B]: Lista de transações
[C]: Lista por categoria 
[D]: Extrato de transações
[E]: Extrato por categoria 
[F]: Atualizar Transação
[G]: Deletar Transação
[H]: Resetar Transações
[I]: Sair
Selecione a opção:''').upper()

    if opcao == 'A':
        adicionar_transacao()
    elif opcao == 'B':
        lista_transacoes()
    elif opcao == 'C':
        lista_categoria()
    elif opcao == 'D':
        extrato_transacoes()
    elif opcao == 'E':
        extrato_categorias()
    elif opcao == 'F':
        atualizar_transacao('data.csv')
    elif opcao == 'G':
        deletar_transacao('data.csv')
    elif opcao == 'H':
        resetar_transacoes('data.csv')
    elif opcao == 'I':
        print("Obrigado por utilizar o Sistema de Rastreamento de Despesas Pessoais!")
        break
    else:
        print("Não foi escolhida uma opção válida")
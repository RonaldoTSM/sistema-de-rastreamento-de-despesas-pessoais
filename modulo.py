def adicionar_transacao():
    lista = []  
    lista.append(input('Adicione um nome à transação: '))
    lista.append(input('Adicione a categoria da transação [contas, entretenimento, saúde, investimento, estudo]: '))

    while True:
        try:
            valor = float(input('Digite o valor da transação [Utilize um sinal - para gastos]: '))
            break
        except ValueError:
            print('Valor inválido. Digite um número válido.')

    lista.append(str(valor))

    linha = ','.join(lista) + '\n'  

    with open('data.csv', 'a', encoding='utf-8') as file:  
        file.write(linha)

def lista_transacoes():
    file = open('data.csv', 'r', encoding='utf-8')
    conteudo = file.readlines()
    file.close()

    tabela = []

    for linha in conteudo:
        
        linha = linha.strip()
         
        campos = linha.split(',')
        tabela.append(campos)

    for linha in tabela:
        print(f"|{linha[0]:<20} |{linha[1]:<20} |{linha[2]:<20} |")

def lista_categoria():
    categorias = ['contas', 'entretenimento', 'saúde', 'investimento', 'estudo']

    while True:
        escolha = input('Qual a categoria que você deseja ver [contas, entretenimento, saúde, investimento, estudo]: ')
        if escolha not in categorias:
            print('Categoria inválida. Digite uma categoria válida [contas, entretenimento, saúde, investimento, estudo]')
        else:
            break 

    with open('data.csv', 'r', encoding='utf-8') as file:
        conteudo = file.readlines()

    tabela = []

    for linha in conteudo:
        linha = linha.strip()
        campos = linha.split(',')
        tabela.append(campos)
    
    print(f"|{'Nome':<20} |{'Categoria':<20} |{'Valor':<20} |")
    
    encontrou_transacoes = False
    for linha in tabela:
        if linha[1].lower() == escolha.lower():
            print(f"|{linha[0]:<20} |{linha[1]:<20} |{linha[2]:<20} |")
            encontrou_transacoes = True

    if not encontrou_transacoes:
        print('Nenhuma transação encontrada para a categoria selecionada.')

def extrato_transacoes():
    total = 0
    file = open('data.csv', 'r', encoding='utf-8')
    conteudo = file.readlines()
    file.close()

    tabela = []

    for linha in conteudo:
        linha = linha.strip()
        campos = linha.split(',')
        tabela.append(campos)

    for linha in tabela[1:]:  
        if len(linha) > 2:
            campo_valor = float(linha[2])
            total += campo_valor

    for linha in tabela:
        print(f'|{linha[0]:<20} |{linha[1]:<20} |{linha[2]:<20}')

    print(f'|total                                      |{total}')

def extrato_categorias():
    categorias = ['contas', 'entretenimento', 'saúde', 'investimento', 'estudo']
    
    while True:
        escolha = input('Qual a categoria que você deseja ver [contas, entretenimento, saúde, investimento, estudo]: ')
        if escolha not in categorias:
            print('Categoria inválida. Digite uma categoria válida [contas, entretenimento, saúde, investimento, estudo]')
        else:
            break 

    total = 0
    file = open('data.csv', 'r', encoding='utf-8')
    conteudo = file.readlines()
    file.close()

    tabela = []

    for linha in conteudo:
        linha = linha.strip()
        campos = linha.split(',')
        tabela.append(campos)

    encontrou_transacoes = False    
    for linha in tabela:           
        if linha[1].lower() == escolha.lower():                        
            print(f"|{linha[0]:<20} |{linha[1]:<20} |{linha[2]:<20}")
            campo_valor = float(linha[2])
            total += campo_valor
            encontrou_transacoes = True

    if encontrou_transacoes:
        print(f"|{'Total':<20} |{'':<20} |{total:<20}")
    else:
        print('Nenhuma transação encontrada para a categoria selecionada.')

def atualizar_transacao(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.readlines()
    
    print("Transações existentes:")
    for i, linha in enumerate(conteudo):
        if i == 0:
            continue  

        campos = linha.strip().split(',')
        print(f"{i}. Nome: {campos[0]}, Categoria: {campos[1]}, Valor: {campos[2]}")
    
    num_transacao = int(input("Digite o número da transação que deseja alterar: "))
    
    if num_transacao <= 0 or num_transacao >= len(conteudo):
        print("Número de transação inválido.")
        return
    
    novo_nome = input("Digite o novo nome: ")
    nova_categoria = input("Digite a nova categoria: ")
    novo_valor = input("Digite o novo valor: ")
    
    campos = conteudo[num_transacao].strip().split(',')
    campos[0] = novo_nome
    campos[1] = nova_categoria
    campos[2] = novo_valor
    nova_linha = ','.join(campos)
    
    conteudo[num_transacao] = nova_linha + '\n'
    
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.writelines(conteudo)

    print('A transação foi alterada com sucesso no arquivo CSV.')

def deletar_transacao(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.readlines()
    
    print("Transações existentes:")
    for i, linha in enumerate(conteudo):
        if i == 0:
            continue  

        campos = linha.strip().split(',')
        print(f"{i}. Nome: {campos[0]}, Categoria: {campos[1]}, Valor: {campos[2]}")
    
    num_transacao = int(input("Digite o número da transação que deseja deletar: "))
    
    if num_transacao <= 0 or num_transacao >= len(conteudo):
        print("Número de transação inválido.")
        return
    
    del conteudo[num_transacao]
    
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.writelines(conteudo)

    print('A transação foi deletada com sucesso do arquivo CSV.')

def resetar_transacoes(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write('')  

    conteudo = "nome,categoria,valor\n"  

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_csv:
        arquivo_csv.write(conteudo)

    print(f'O arquivo CSV "{nome_arquivo}" foi resetado com sucesso.')

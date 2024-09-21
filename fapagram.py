perfis = ["Lucca", "JoãoWobeto", "Moreira", "Samuel", "EduardoMesser"] #lista guardando os usuários pré-definidos
#lista guardando as conexões de cada usuário, 1 = seguindo , 0 = não segue | cada linha é um usuário, ex: linha 1 = lucca, linha 4 = samuel
rede = [[0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0]]

#duas listas pré-definidas conforme as conexões de cada usuário acima
seguidores = [4, 4, 1, 3, 1]
seguindo = [3, 2, 2, 2, 4]

def total_perfis(rede): #função para retornar a quantidade de perfis existentes 
    return len(rede) #a função len vai me retornar a quantidade de listas (usuários) dentro da minha rede

def conexoes(rede): #função para retornar o número de conexões existentes
    conexoes = 0 #variável acumuladora
    for linha in rede:
        conexoes += sum(linha) #para cada linha dentro da minha rede, vai somando os valores encontrados na minha variavel conexoes, ex: primeira linha = 3
    return conexoes

def centralidade(perfil_index, rede): #função para retornar a centralidade de um determinado perfil
    centralidade = 0 #variável acumuladora
    for j in range(len(rede)): #percorre todos os indices da lista verificando conexoes
        if rede[perfil_index][j] == 1 and rede[j][perfil_index] == 1: #verifica se existe uma conexao entre o perfil indicado e o usuario no indice j
            centralidade += 1 #se tiver conexao entre ambos, acumula valor a centralidade do usuario
    return centralidade

def densidade(rede): #função para calcular a densidade da rede
    qtd_conex = 0 #variável acumuladora
    qtd_perfis = len(rede) #total de perfis = total de listas na rede
    for i in range(qtd_perfis): #percorre cada um dos perfis
        qtd_conex += sum(rede[i]) #acumula o total de conexoes de cada perfil, conforme o i
    qtd_conex //= 2 #cada conexao é contado duas vezes, e divide por 2, resultando no número real de conexoes unicas
    qtd_max_conex = qtd_perfis * (qtd_perfis - 1) // 2 #calcula o numero maximo possivel de conexoes, sendo que cada perfil pode se conectar a todos, exceto ele mesmo
    if qtd_max_conex > 0: #verifica conexoes existentes
        return qtd_conex / qtd_max_conex 

def lista_ordenada(rede, perfis, seguidores, seguindo): #função para ordenar a lista em ordem decrescente
    perfis_centralidade = [] #lista para armazenar a centralidade de cada perfil
    for i in range(len(rede)): #percorre cada perfil
        conexoes = sum(rede[i]) #calcula o total de conexoes de cada perfil, somando os valores da linha do mesmo na matriz
        conex_mutua = 0 #variável acumuladora
        for j in range(len(rede)): #percorre o restante dos perfis
            if rede[i][j] == 1 and rede[j][i] == 1: #verifica se existe uma conexao mutua entre dois perfis
                conex_mutua += 1 #se existir uma conexao mutua, acrescenta a variavel
        perfis_centralidade.append((perfis[i], conexoes, seguindo[i], seguidores[i], conex_mutua)) #cria uma tupla com o nome do perfil e as metricas
    
    i = 0
    while i < len(perfis_centralidade) - 1: #percorre todos os perfis até o penultimo
        j = i + 1 #permite a lista percorre ate o ultimo indice, sem chances de acessar um indice fora da lista
        while j < len(perfis_centralidade): #compara os usuarios
            #se o perfil i tiver menos conexoes que o perfil j = troca
            if perfis_centralidade[i][4] <  perfis_centralidade[j][4]: 
                troca = perfis_centralidade[i] #variável temporária
                perfis_centralidade[i] = perfis_centralidade[j]
                perfis_centralidade[j] = troca
            j += 1
        i += 1
    print("Lista de perfis ordenados por número de conexões mútuas:")
    for perfil in perfis_centralidade: #para cada perfil dentro da minha lista, imprime para todos ordenadamente
        print(f"Usuário {perfil[0]} possui {perfil[4]} conexões mútuas | {perfil[2]} seguindo, {perfil[3]} seguidores")

def atualizar_rede(rede, perfis, tipo_atualizacao, perfil1=None, perfil2=None):
    if tipo_atualizacao == "adicionar_perfil":
        novo_perfil = input("Informe o nome do perfil que deseja cadastrar: ")
        perfis.append(novo_perfil)
        seguidores.append(0)
        seguindo.append(0)
        for linha in rede:
            linha.append(0)
        rede.append([0] * len(rede[0])) #adiciona uma nova linha para a minha matriz, referente ao novo usuario, sem nenhuma conexao
        print(f"O perfil {novo_perfil} foi adicionado com sucesso!")

    elif tipo_atualizacao == "remover_perfil":
        perfil_removido = perfis[perfil1]
        perfis.pop(perfil1)
        seguidores.pop(perfil1)
        seguindo.pop(perfil1)
        rede.pop(perfil1)
        for linha in rede:
            linha.pop(perfil1)
        print(f"O perfil {perfil_removido} foi removido com sucesso!")

    elif tipo_atualizacao == "adicionar_conexao":
        rede[perfil1][perfil2] = 1
        seguindo[perfil1] += 1
        seguidores[perfil1] += 1
        print(f"{perfis[perfil1]} começou a seguir {perfis[perfil2]}.")

    elif tipo_atualizacao == "remover_conexao":
        rede[perfil1][perfil2] = 0
        seguindo[perfil1] -= 1
        seguidores[perfil1] -= 1
        print(f"{perfis[perfil1]} parou de seguir {perfis[perfil2]}.")
    
    lista_ordenada(rede, perfis, seguidores, seguindo)

def nome_app():
    print("""█▀▀ ▄▀█ █▀█ ▄▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█▀░ █▀█ █▀▀ █▀█ █▄█ █▀▄ █▀█ █░▀░█\n""")
    
def retornar_menu():
    input("\nDigite uma tecla para retornar ao menu principal")
    menu()

def menu():
    while True:
        nome_app()
        print("Selecione a ação desejada:")
        print("\n1. Número de perfis da rede")
        print("2. Número de conexões da rede")
        print("3. Centralidade da rede")
        print("4. Densidade da rede")
        print("5. Lista ordenada dos perfis por número de conexões")
        print("6. Atualizar a rede")
        print("0. Sair\n")

        acao = int(input("Selecione a opção desejada: "))

        if acao == 1:
            nome_app()
            print(f"Quantidade de perfis na rede: {total_perfis(rede)}")
            retornar_menu()
        elif acao == 2:
            nome_app()
            print(f"Número de conexões da rede: {conexoes(rede)}")
            retornar_menu()
        elif acao == 3:
            nome_app()
            perfil = input("Informe o perfil: ")
            if perfil in perfis:
                perfil_index = perfis.index(perfil)
                conexao = centralidade(perfil_index, rede)
                print(f"Centralidade do perfil do usuário {perfil}: {conexao} conexões")
            retornar_menu()
        elif acao == 4:
            nome_app()
            densidade_rede = densidade(rede)
            print(f"Densidade da rede: {densidade_rede:.2f}")
            retornar_menu()
        elif acao == 5:
            nome_app()
            lista_ordenada(rede, perfis, seguidores, seguindo)
            retornar_menu()
        elif acao == 6:
            nome_app()
            print("1. Adicionar perfil")
            print("2. Remover perfil")
            print("3. Adicionar conexão")
            print("4. Remover conexão")
            escolha = int(input("\nEscolha uma das opções acima: "))
            if escolha == 1:
                atualizar_rede(rede, perfis, "adicionar_perfil")
            elif escolha == 2:
                perfil_removido = input("Informe o perfil a ser removido: ")                
                if perfil_removido in perfis:
                    perfil_removido = perfis.index(perfil_removido)
                    atualizar_rede(rede, perfis, "remover_perfil", perfil_removido)
            elif escolha == 3:
                perfil1 = input("Informe o nome do usuário: ")
                perfil2 = input("Informe o nome do usuário que deseja seguir: ")
                user1 = perfis.index(perfil1)
                user2 = perfis.index(perfil2)
                atualizar_rede(rede, perfis, "adicionar_conexao", user1, user2)
            elif escolha == 4:
                perfil1 = input("Informe o nome do usuário: ")
                perfil2 = input("Informe o nome do usuário que deseja deixar de seguir: ")
                user1 = perfis.index(perfil1)
                user2 = perfis.index(perfil2)
                atualizar_rede(rede, perfis, "remover_conexao", user1, user2)
            else:
                print("Opção inválida\nRetornando ao menu principal...")
                menu()
        elif acao == 0:
            print("Desconectando...")
            break
        else:
            print("Opção inválida. Tente novamente!")
menu()
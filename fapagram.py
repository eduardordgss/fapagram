perfis = ["Alice", "Sabrina", "Olivia", "Inacio", "Joaquim"]
rede = [[0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0]]

seguidores = [4, 4, 1, 3, 1]
seguindo = [3, 2, 2, 2, 4]

def total_perfis(rede):
    return len(rede)

def conexoes(rede):
    conexoes = 0
    for linha in rede:
        conexoes += sum(linha)
    return conexoes

def centralidade(perfil_ind, rede):
    centralidade = 0
    for j in range(len(rede)):
        if rede[perfil_ind][j] == 1 and rede[j][perfil_ind] == 1:
            centralidade += 1
    return centralidade

def densidade(rede):
    qtd_conex = 0
    qtd_perfis = len(rede)
    for i in range(qtd_perfis):
        for j in range(i+1, qtd_perfis):
            if rede[i][j] == 1 and rede[j][i] == 1:
                qtd_conex += 1
    qtd_max_conex = qtd_perfis * (qtd_perfis - 1) / 2
    if qtd_max_conex > 0:
        return qtd_conex / qtd_max_conex

def lista_ordenada(rede, perfis, seguidores, seguindo):
    perfis_centralidade = []
    for i in range(len(rede)):
        conexoes = sum(rede[i])
        conex_mutua = 0
        for j in range(len(rede)):
            if rede[i][j] == 1 and rede[j][i] == 1:
                conex_mutua += 1
        perfis_centralidade.append((perfis[i], conexoes, seguindo[i], seguidores[i], conex_mutua))

    i = 0
    while i < len(perfis_centralidade) - 1:
        j = i + 1
        while j < len(perfis_centralidade):
            if perfis_centralidade[i][4] <  perfis_centralidade[j][4]:
                troca = perfis_centralidade[i]
                perfis_centralidade[i] = perfis_centralidade[j]
                perfis_centralidade[j] = troca
            j += 1
        i += 1
    print("Lista de perfis ordenados por número de conexões mútuas:")
    for perfil in perfis_centralidade:
        print(f"Usuário @{perfil[0]} possui {perfil[4]} conexões mútuas | {perfil[2]} seguindo, {perfil[3]} seguidores")

def atualizar_rede(rede, perfis, tipo_atualizacao, perfil1=None, perfil2=None):
    if tipo_atualizacao == "adicionar_perfil":
        novo_perfil = input("Informe o nome do perfil que deseja cadastrar: ")
        perfis.append(novo_perfil)
        seguidores.append(0)
        seguindo.append(0)
        for linha in rede:
            linha.append(0)
        rede.append([0] * len(rede[0]))
        print(f"O perfil @{novo_perfil} foi adicionado com sucesso!")

    elif tipo_atualizacao == "remover_perfil":
        perfil_removido = perfis[perfil1]
        perfis.pop(perfil1)
        seguidores.pop(perfil1)
        seguindo.pop(perfil1)
        rede.pop(perfil1)
        for linha in rede:
            linha.pop(perfil1)
        print(f"O perfil @{perfil_removido} foi removido com sucesso!")

    elif tipo_atualizacao == "adicionar_conexao":
        rede[perfil1][perfil2] = 1
        seguindo[perfil1] += 1
        seguidores[perfil2] += 1
        print(f"@{perfis[perfil1]} começou a seguir @{perfis[perfil2]}.")

    elif tipo_atualizacao == "remover_conexao":
        rede[perfil1][perfil2] = 0
        seguindo[perfil1] -= 1
        seguidores[perfil2] -= 1
        print(f"@{perfis[perfil1]} parou de seguir @{perfis[perfil2]}.")

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
                perfil_ind = perfis.index(perfil)
                conexao = centralidade(perfil_ind, rede)
                print(f"Centralidade do perfil do usuário @{perfil}: {conexao} conexões")
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
                if perfil1 == perfil2:
                    print("O usuário não pode seguir a si próprio")
                    print("Retornando ao menu principal...")
                    menu()
                else:
                    user1 = perfis.index(perfil1)
                    user2 = perfis.index(perfil2)
                    atualizar_rede(rede, perfis, "adicionar_conexao", user1, user2)
            elif escolha == 4:
                perfil1 = input("Informe o nome do usuário: ")
                perfil2 = input("Informe o nome do usuário que deseja deixar de seguir: ")
                if perfil1 == perfil2:
                    print("O usuário não segue a si próprio")
                    print("Retornando ao menu principal...")
                    menu()
                else:
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
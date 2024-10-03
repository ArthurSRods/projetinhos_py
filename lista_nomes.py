def lista_nomes():
    cont = 0
    tamanho_lista = 100
    nomes = ["vazio" for i in range(tamanho_lista)] 
        
    resposta = input("Deseja preencher a lista de nomes? Se SIM, digite (S), se NÃO, digite (N): ")

    while resposta.lower() == 's':
        if cont < tamanho_lista:
            nome = input("Vamos começar. Digite o nome: ")
            nomes[cont] = nome
            cont += 1
            resposta = input("Deseja continuar o preenchimento da lista de nomes? Se SIM, digite (S), se NÃO, digite (N): ")
        else:
            print("A lista está cheia!")
            break

    print(f"Fim da lista. Você possui {cont} nome(s), são eles:")
    for nome in nomes:
        if nome != "vazio":
            print(nome)

lista_nomes()

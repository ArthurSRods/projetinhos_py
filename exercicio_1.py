###EXERCICIO
primeiro_valor = input('Digite um valor ')
segundo_valor = input('Digite um valor ')
if primeiro_valor>=segundo_valor:
    print(f'{primeiro_valor} é maior ou igual que {segundo_valor}.')
elif segundo_valor>=primeiro_valor:
    print(f'{segundo_valor} é maior ou igual que {primeiro_valor}.')
else:
    print('Tente novamente.')

#DEU CERTINHO!!!

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome=input('Digite seu nome ')
idade=input('Digite sua idade ')
if nome and idade:
    nome_invertido=nome[::-1]
    print(f'Seu nome invertido é {nome_invertido}')
    tem_espaços= ' ' in nome
    if tem_espaços == True: print(f'{nome} tem espaços.')
    else: print (f'{nome} não tem espaços')
    tamanho=len(nome)
    print(f'Seu nome tem {tamanho} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')
else: print("Desculpe, você deixou campos vazios.")
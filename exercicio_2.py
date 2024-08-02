"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_int = None
while numero_int is None:
    try: numero_int = int(input('Digite um numero inteiro '))
    except ValueError: print('O valor digitado não corresponde a um número inteiro. ')
if int(numero_int)%2==0:
    print (f'{numero_int} é par.')
elif int(numero_int)%2!=0:
    print (f'{numero_int} é impar.')

###RESOLUÇÃO ALTERNATIVA###
entrada=input('Digite um número inteiro ')
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
nome_usuario=input('Olá, digite seu nome de usuário ')
horas = None
while horas is None:
    try: horas=int(input(f'Olá {nome_usuario}, vc sabe me dizer que horas são?'))
    except ValueError: print('Desculpe, tente novamente.')
if 0<=horas<=11:
    print(f'Bom dia {nome_usuario}')
if 12<=horas<=17:
    print(f'Boa tarde {nome_usuario}')
if 18<=horas<=23:
    print(f'Boa noite {nome_usuario}')

###RESOLUÇÃO ALTERNATIVA###
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome=input('Digite seu nome: ')
if len(nome)<=4:
    print('Seu nome é curto.')
    print(f'Seu nome tem {len(nome)} letras')
elif 5<=len(nome)<=6:
    print('Seu nome é normal.')
    print(f'Seu nome tem {len(nome)} letras')
elif len(nome)>6:
    print('Seu nome é muito grande.')
    print(f'Seu nome tem {len(nome)} letras')
else:
    print('Algo errado não está certo.')
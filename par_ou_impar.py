import random

def par_ou_impar():
    escolha_maquina = None
    escolha_jogador = input('Olá usuário, vamos jogar uma partida de par ou impar? \nVocê quer ser par ou ímpar? ')
    
    if escolha_jogador == 'par':
        print('Vc escolheu par. ')
        escolha_maquina = 'impar'
    elif escolha_jogador == 'impar':
        print('Vc escolheu impar. ')
        escolha_maquina = 'par'
    else: print('Tente novamente. ')
    
    numero_jogador = int(input('Digite o numero que vc quer jogar: '))
    numero_maquina = random.randint(1,5)
    print(f'A máquina jogou {numero_maquina}')

    resultado = (numero_jogador+numero_maquina)%2
    if resultado == 0 : 
        resultado = 'par'
        print('Deu par! ')
    elif resultado != 0 :
        resultado = 'impar'
        print('Deu impar! ')
    
    if resultado == escolha_jogador:
        print('O jogador ganhou! ')
    elif resultado == escolha_maquina:
        print('O computador ganhou! ')

par_ou_impar()



#CALCULO DO IMC
def calculadora_imc():
    nome=input('Qual o seu nome? ')
    idade=input(f'{nome} qual sua idade? ')
    peso= None
    while peso is None:
        try: peso = float(input('Quanto você pesa? '))
        except ValueError: ('Tente novamente.')
    altura= None
    while altura is None:
        try: altura = float(input('Qual sua altura? '))
        except ValueError: ('Tente novamente.')
    imc= peso/(altura)**2
    return (f'{nome} seu IMC é de {imc:.2f}')

print(calculadora_imc())
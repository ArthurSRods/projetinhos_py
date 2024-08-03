cotacao_dolar = None
valor_dolar = None
valor_real = None

opcao_conversao = int(input('Você quer converter real para dolar ou dolar para real? \n Se quiser converter de real para dolar, digite 1.\n Se quiser converter de dolar para real, digite 2.\n'))
while cotacao_dolar is None: 
        try: cotacao_dolar = float(input('Qual a cotação do dolar atual? '))
        except ValueError: print("Tente novamente.")
if opcao_conversao == 1:
    while valor_real is None: 
        try: valor_real = float(input('Qual o valor em reais você quer converter? '))
        except ValueError: "Tente novamente."
    valor_dolar = valor_real / cotacao_dolar
    print(f'Na cotação atual, o valor será de US$ {valor_dolar:.2f}. ')
elif opcao_conversao == 2:
    while valor_dolar is None: 
        try: valor_dolar = float(input('Qual o valor em dolar você quer converter? '))
        except ValueError: "Tente novamente."
    valor_real = cotacao_dolar * valor_dolar
    print(f'Na cotação atual, o valor será de R$ {valor_real:.2f}. ')
else:
    print("Opção inválida. Tente novamente.")

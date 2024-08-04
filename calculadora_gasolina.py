def calculadora_gasolina():
    distancia= None
    while distancia is None:
        try: distancia = float(input('Qual a distancia? ')) 
        except ValueError: "Tente de novo"
    distancia_ida_e_volta=float(distancia)*2 
    km_por_l=input('Quantos km seu veículo faz com 1L? ')
    gasolina_pra_ir=float(distancia)/float(km_por_l)
    gasolina_ida_e_volta=distancia_ida_e_volta/float(km_por_l)
    preço_gasolina=input('Quanto tá a gasolina? ')
    valor_da_brincadeira=float(preço_gasolina)*(gasolina_ida_e_volta)
    print(f'De gasolina, ida e volta, vc irá gastar {gasolina_ida_e_volta:.2f} L')
    print(f'A viagem vai custar R${valor_da_brincadeira:.2f}')

calculadora_gasolina()
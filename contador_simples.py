#CONTADOR SIMPLES
def contador():
    print('Olá, vou contar até um valor x.')
    valor = int(input('Até que valor devo contar? '))
    contador = 0
    while contador < valor:
        contador += 1 
        print(contador)
    print('Acabou ')
contador()

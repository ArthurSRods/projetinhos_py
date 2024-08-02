nota_P1=input('Qual foi sua nota na P1? ')
nota_P2=input('Qual foi sua nota na P2? ')
nota_P3=input('Qual foi sua nota na P3? ')
soma_P=float(nota_P1)+float(nota_P2)+float(nota_P3)
media_P=soma_P/3
if media_P<5:print(f'Sua nota foi {media_P:.1f}. Você está reprovado.')
else:
    if media_P==5:print(f'Sua nota foi {media_P:.1f}. Você passou na média.')
    else:
        if 5<media_P<9:print(f'Sua nota foi {media_P:.1f}. Você foi aprovado.')
        elif media_P>=9:print(f'Parabéns! Sua nota foi {media_P:.1f}. Você passou!')
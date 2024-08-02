#EXERCICIO QUE RECEBI DO MEU AMIGO GOES PARA PRATICAR
# Você vai pedir pro usuário escrever o nome dele pra você
# a) você vai responder pra ele quantas letras tem
# b) se é par ou impar
# c) mandar pra ele de tras pra frente o nome de volta
# d) devolver cada letra individualmente

nome=input('Digite seu nome: ')
n_letras=len(nome)
print(n_letras) # Utiliza-se a função len para contar caracteres.
if n_letras % 2 == 0: print ('É par') # É possível verificar se um numero é par ou impar divindo ele por 2. Se o resto for 0, ele será par.
else: print('É impar')

for i in range (n_letras):
    c=nome[n_letras -1 -i]
    print(c.lower()) # lower para caracteres minusculos
for i in range (n_letras): #para cada i (indice) que eu tiver no range (comprimento) do nome, eu terei:
    c=nome[n_letras -1 -i] #c vai ser o caractere de nome -1 (pq os indices variam de 0 a 9, então começa a contar do 0) e -i para devolver de trás pra frente.
    print(c.upper()) # upper para caracteres maiusculos

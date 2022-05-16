# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# Importação de bibliotecas.
from random import choice

# Cadastro de alunos.
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Listagem dos alunos.
alunos = [n1, n2, n3, n4] #Para o paython uma lista fica entre cochetes

#Imprime relatório
print('O aluno escolhido hoje é {}!'.format(choice(alunos)))


'''# Importação de bibliotecas.
from random import choice

# Relação de alunos
alunos = (['Thiago', 'Pedro', 'João', 'Maria'])

# Imprime relatório
print('O aluno escolhido hoje é {}'.format(choice(alunos)))'''


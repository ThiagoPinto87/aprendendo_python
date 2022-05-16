# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importação de bibliotecas
from random import shuffle

# Cadastrando alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Relação de alunos
alunos = [n1, n2, n3, n4]
shuffle(alunos)
# Sortea a lista
print('A sequencia dos alunos para apresentar o trabalho é')
print(alunos)


# Outra maneira de fazer o resultado 3/2.

'''# Importação de bibliotecas
from random import sample

# Cadastrando alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Relação de alunos
alunos = [n1, n2, n3, n4]

# Sortea a lista
print('A sequencia dos alunos para apresentar o trabalho é {}'.format(sample(alunos, k=4)))'''



#Outra forma de se resolver a solução 3/3.

'''# Importação de bibliotecas
from random import sample

# Relação de alunos
alunos = ('Thiago', 'Guanabara', 'João', 'Maria')

# Sortea a lista
print('A sequencia dos alunos para apresentar o trabalho é {}'.format(sample(alunos, k=4)))'''
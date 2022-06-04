""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves."""
# FIZ ERRADO O EXERCÍCIO, EU NÃO COLOQUEI OS RESULTADOS EM UMA ÚNICA LISTA.

triagem = []
pessoas = []
maior = menor = 0
while True:
    triagem.append(str(input('Digite o nome: ')).strip().upper())
    triagem.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = triagem[1]
    elif triagem[1] > maior:
        maior = triagem[1]
    elif triagem[1] < menor:
        menor = triagem[1]
    pessoas.append(triagem[:])
    triagem.clear()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-=' * 20)
#print(f'Os dados digitados foram: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. ', end='Das pessoas: ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. ', end='Das pessoas: ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')











"""# Criação das listas e variáveis iniciais
pessoas_pesadas = []
pessoas_leves = []
triagem = []
resp = 'S'
cont = 0
# Laço de repetição com flag de parada.
while True:
    if resp == 'S':
        # Captura das informações
        triagem.append(input('Digite o nome de uma pessoa: ').strip().upper())
        triagem.append(int(input('Digite o peso dela (em Kg): ')))
        cont += 1

        # Analisa a triagem e envia a informação da pessoa para a lista correspondente.
        if triagem[1] > 100:
            pessoas_pesadas.append(triagem[:])
            triagem.clear()
        else:
            pessoas_leves.append(triagem[:])
            triagem.clear()
        resp = str(input('Quer continuar a lançar? [S/N]: ')).strip().upper()[0]
    else:
        break
# Imprime os relatórios
print('-=' * 20)
# Informa a quantidade de pessoas cadastradas
print(f'Foram cadastradas {cont} pessoas.')
print('-' * 40)
# Informa os resultados das listas de pessoas pesadas e leves
print(f'As pessoas mais pesadas são:')
# Laço de repetição com flag de parada nas listas.
for pp in pessoas_pesadas:
    print(f'- {pp[0]} que pesou {pp[1]}Kg.')
print('-' * 40)
# Laço de repetição com flag de parada nas listas.
print(f'As pessoas mais leves são:')
for pl in pessoas_leves:
    print(f'- {pl[0]} que pesou {pl[1]}Kg.')
"""
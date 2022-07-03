""" Crie um programa que leia nome, sexo e idade de várias pessoas guardando os dados de cada pessoa em um dicionário,
e todos os dicionários em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média."""

# Cria a lista de armazenamento
cadastro = list()

while True:  # Armazenamento de pessoas dentro da lista cadastro.
    # Cria o dicionário de cadastro das pessoas
    pessoas = dict()
    pessoas['nome'] = str(input('Nome: ')).strip().upper()
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':  # Validação de sexo.
        print('ERRO! Por favor, responda com "M" ou "F".')
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    while pessoas['idade'] < 0 or pessoas['idade'] > 120:  # Validação de idade.
        print('ERRO! Por favor, responda com idade entre 0 e 120 anos.')
        pessoas['idade'] = int(input('Idade: '))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'SN':  # Validação de resposta.
        print('ERRO! Por favor responda com "S" ou "N".')
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    cadastro.append(pessoas.copy())
    if resposta == 'N':  # Verificação para flag de parada para início dos relatórios.
        break

print('-=' * 30)

# Mostra quantas pessoas foram cadastradas.
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')

# Retorna a média de idade das pessoas cadastradas.
soma_idade = media_idade = cont = 0
for p in cadastro:
    soma_idade += cadastro[cont]['idade']
    cont += 1
media_idade = soma_idade / len(cadastro)
print(f'B) A média de idade das pessoas cadastradas é: {media_idade:.2f} anos.')

# Retorna o nome das mulheres cadastradas.
mulheres = list()
cont = 0
for m in cadastro:
    if cadastro[cont]['sexo'] == 'F':
        mulheres.append(cadastro[cont]['nome'])
    cont += 1
print(f'C) As mulheres cadastradas são: {mulheres}.')

# Retorna o nome das pessoas com idade superior a média.
acima_media = list()
cont = 0
for x in cadastro:
    if cadastro[cont]['idade'] > media_idade:
        acima_media.append(cadastro[cont]['nome'])
    cont += 1
print(f'D) As pessoas com idade acima da média são: {acima_media}')




""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos."""

# Aglutina ou seta as variáveis iniciais como 0 ou vazias.
soma_idade = 0
menor_idade = 0
sexo = ''
maior_idade = 0
nome_velho = ''

# Cria laço de 4 resultados.
for pessoa in range(1, 5):
    print('---- Dados {}ª Pessoa ----'.format(pessoa))
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    # Soma as idades das pessoas.
    soma_idade += idade

    # Verifica o nome do homem mais velho e subistitui os resultados das variáveis "maior_idade" e "nome_velho" quando os resultados coincidem com as condições.
    if pessoa == 1 and sexo == 'M':  # Para não ter a necessidade de colocar no "sexo" o atributo ".upper()", a string dessa linha poderia ser "... sexo in 'Mm'"
        maior_idade = idade
        nome_velho = nome
    elif sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

    # Verifica quantas mulheres tem menos de 20 anos.
    if sexo == 'F' and idade < 70:
        menor_idade += 1


print('A média da idade do grupo é de {:.0f} anos'.format(soma_idade / 4))
print('O nome do homem mais velho é {} pois tem {} anos'.format(nome_velho, maior_idade))
print('No grupo há {} mulheres menores que 70 anos.'.format(menor_idade))

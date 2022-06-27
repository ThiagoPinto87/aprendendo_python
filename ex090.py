""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""


# Iterações iniciais ou zeradas
ficha = dict()  # Cria a ficha do aluno.
media = 0  # Cria a variável media e seta o valor 0.

# Captura as informações do aluno.
ficha['nome'] = str(input('Nome do aluno: ')).upper().strip()  # Cria a key 'nome' e solicita input.
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))  # Cria a key media e solicita input.

# Verifica a situação do aluno.
if ficha['media'] >= 7:
    ficha['resultado'] = 'APROVADO'
elif ficha['media'] <= 5:
    ficha['resultado'] = 'REPROVADO'
elif ficha['media'] > 5 and ficha['media'] < 7:  # Essa strig poderia ter sido escrita elif 5 <= ficha['media'] < 7
    ficha['resultado'] = 'RECUPERAÇÃO'

# Imprime o resultado.
print('-=' * 15)
print(f'- O nome do aluno é {ficha["nome"]}.')
print(f'- A média de {ficha["nome"]} é: {ficha["media"]}')
print(f'- A situação é {ficha["resultado"]}!')

# Após ver a aula do professor guanabara, vou fazer a solução igual ao dele.

print('-=' * 15)
print('-=-=-=-FORMA GUANABARA-=-=-=-')
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')

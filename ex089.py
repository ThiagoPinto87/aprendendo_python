""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar notas de cada aluno
individualmente."""

# Listas Instantes zeradas e iniciais.
basedados = list()  # Cria lista com todas os registros dos alunos.
registro = list()  # Cria os registros dos alunos com notas e média.
resposta = 'S'  # Instante inicial para flag de parada.
pesquisa = 0  # Instante zerada para flag de parada.

# Recebe os registros de cada aluno e adiciona na lista base de dados.
while resposta == 'S':  # Laço de repetição com flag de parada.
    nome = str(input('Digite o nome do aluno: ')).strip().upper()  # Registra o nome do aluno.
    nota1 = float(input('Nota 1: '))  # Registra a primeira nota do aluno.
    nota2 = float(input('Nota 2: '))  # Registra a segunda nota do aluno.
    media = (nota1 + nota2) / 2  # Calcula a média do aluno.
    registro.append(nome)  # Insere o nome do aluno à lista registro.
    registro.append(nota1)  # Insere a primeira nota do aluno à lista registro.
    registro.append(nota2)  # Insere a segunda nota do aluno à lista registro.
    registro.append(media)  # Insere a média do aluno à lista registro.
    resposta = str(input('Deseja continuar? ')).strip().upper()[0]  # Verifica se o usuário quer continuar digitando.
    if resposta not in 'SN':  # Laço de repetição com flag de parada caso o usuário digite algo indesejado.
        print('Informação inválida! Por favor responda a pergunta corretamente.')  # Informa input indesejado.
        resposta = str(input('Deseja continuar? ')).strip().upper()[0]  # Refaz a pergunta ao usuário quanto a continuar.
    basedados.append(registro[:])  # Insere cópia da lista registo à lista base de dados. Atenção para [:] importante.
    registro.clear()  # Limpa as informações da variável registro.
print('-=' * 15)  # Margem de ornamentação.
print(f'{"No.":<4}{"NOME":<15}{"MEDIA":>4}')  # Cria o cabeçalho da tabela.
print('-' * 30)  # Margem de ornamentação.
for i, a in enumerate(basedados):  # Laço de repetição com verificação de índice para inserção na tabela.
    print(f'{i:<4}{a[0]:<15}{a[3]:>4.1f}')  # Imprime as informações da base de dados já formatando em tabela.
print('-' * 30)  # Margem de ornamentação.
while pesquisa != 999:  # Laço de repetição com flag de parada.
    pesquisa = int(input('Digite No. para ver as notas ou 999 para finalizar: '))  # Verificação do número para que se possa verificar a nota do aluno e tambem serve de flag de parada ao digitar 999.
    if pesquisa <= len(basedados) - 1:  # Verifica se a variável pesquisa é menor que o tamanho da base de dados e já verifica qual nota do aluno será impressa.
        print(f'Notas de {basedados[pesquisa][0]} são: {basedados[pesquisa][1]} e {basedados[pesquisa][2]}.')  # Imprime nota do aluno.
        print()  # Para pular linha.
print('-=' * 30)  # Margem de ornamentação.
print('PROGRAMA FINALIZADO!!!')  # Demonstra a finalização do programa.

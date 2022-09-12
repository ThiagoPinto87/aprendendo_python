from ex115.lib.arquivo import *
from ex115.lib.interface import *
from time import sleep


# Cria o arquivo de texto que servirá como "banco de dados"
banco_dados = 'banco_dados.txt'

if not arquivo_bd_existe(banco_dados):  # Verifica se o arquivo está criado e caso não esteja, ele o criará.
    criar_arquivo(banco_dados)


# Menu do sistema
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo.
        ler_arquivo(banco_dados)
    elif resposta == 2:
        cabeçalho('CADASTRAR PESSOAS')
        nome = str(input('Nome: ')).upper()
        idade = leia_int('Idade: ')
        cadastrar(banco_dados, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\33[1;31mERRO! por favor, digite uma opção válida.\33[m')
    sleep(1.5)

from ex115.lib.interface import *


def arquivo_bd_existe(nome_arquivo):  # A idéia dessa função é retornar como verdadeiro ou falso.
    try:
        abrir = open(nome_arquivo, 'rt')  # Verifica se o arquivo existe. O "rt" quer dizer leia texto, com isso,
        abrir.close()
        # ele acaba verificando se o arquivo existe.
    except FileNotFoundError:
        return False
    else:
        print('Sistema carregado corretamente.')
        return True


def criar_arquivo(nome_arquivo):
    try:
        criando = open(nome_arquivo, 'wt+')  # O parâmetro "wt" quer dizer escreva texto, o "+" quer dizer crie caso
        criando.write('NOME;IDADE\n')
        # não tenha o arquivo.
        criando.close()
    except:
        print('Não foi possível criar o banco de dados.')
        print('Favor contactar o desenvolvedor.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso.')


def ler_arquivo(nome_arquivo):
    try:
        lendo = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
        print('Contacte o suporte.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for i in lendo:
            lançamento = i.split(';')
            lançamento[1] = lançamento[1].replace('\n', '')
            print(f'{lançamento[0]:<30}{lançamento[1]:>3}')
    finally:
        lendo.close()


def cadastrar(nome_arquivo, nome='DESCONHECIDO', idade=0):
    try:
        cadastrando = open(nome_arquivo, 'at')  # O "at" quer dizer que ele abrirá pra escrever inserindo ao final.
    except:
        print('ERRO ao abrir o arquivo ao cadastrar pessoas.')
    else:
        try:
            cadastrando.write(f'{nome};{idade}\n')
        except:
            print('Erro! Não foi possivel cadastrar e pessoa.')
        else:
            print(f'{nome} cadastrado com sucesso.')
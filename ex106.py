"""Faça um minisistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra fim, o programa se encerrará.
OBS: use cores."""

from time import sleep


def titulo(msg):
    tam_margem = len(msg) + 12
    print('\33[1;30;42m#' * tam_margem)
    print('     ', msg)
    print('#' * tam_margem)
    print('\33[m ')


def subtitulo(msg):
    tam_margem = len(msg) + 12
    print('\33[30;44m ' * tam_margem)
    print(msg)
    print(' ' * tam_margem)
    print('\33[m')
    sleep(2)


def comentario(msg):
    print(msg)


# Programa Principal
titulo('CONHECENDO O PYTHON')
comentario('Sistema de info do Python!')
info = ''
while True:
    info = str(input('\33[30;42mQual função ou comando procura?\33[m'))
    subtitulo(f'Buscando informações de "{info}".')
    if info.upper() == 'FIM':
        break
    else:
        help(info)
print('\33[30;41mATÉ MAIS!!!\33[m')


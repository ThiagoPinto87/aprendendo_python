from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1 selecionada')
    elif resposta == 2:
        cabeçalho('Opção 2 selecionada')
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\33[1;31mERRO! por favor, digite uma opção válida.\33[m')
    sleep(2.5)



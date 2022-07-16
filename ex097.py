""" Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável
ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~"""

def escreva(txt):
    print('~~'+'~' * len(txt)+'~~')
    print('  '+txt)
    print('~~'+'~' * len(txt)+'~~')


# Programa principal
'''escreva(str(input('Digite o texto: ').upper()))'''
escreva('Mensagem personalizada')


# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#Forma do prof. Guanabara com floreio de importar a biblioteca datetime para pegar o ano do computador.
# Captura o ano a ser verificado

ano = int(input('Qual o ano quer que seja analisado? (Para analisar o ano atual digite 0) :'))
from datetime import date
# Calcula se o ano é bissexto.
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}, é Bissexto!'.format(ano))
else:
    print('O ano de {}, NÃO é Bissexto!'.format(ano))



'''
# Forma que encontrei para resolver o problema.
# Gostei mais da forma do prof. Guanabara. Mais simples e objetivo.
# Captura o ano a ser verificado
ano = int(input('Digite o ano a ser verificado: '))

# Calcula se o ano é bissexto.
calc_1 = ano % 4
if calc_1 == 0:
    calc_2 = ano % 100
    if calc_2 != 0:
        print('O ano de {}, é Bissexto!'.format(ano))
    else:
        calc_3 = ano % 400
        if calc_3 == 0:
            print('O ano de {}, é Bissexto!'.format(ano))
        else:
            print('O ano de {}, NÃO é Bissexto!'.format(ano))

else:
    print('O ano de {}, NÃO é Bissexto!'.format(ano))'''

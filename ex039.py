"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

O programa deverá também mostrar o tempo que falta ou que passou do prazo."""

#Importação de bibliotecas
from datetime import date

#Captura o ano de nascimento
cidadao = int(input('Qual o ano de nascimento? '))

#Captura o ano corrente do computador
ano = date.today().year

#Avalia e emite o relatório.
if ano - cidadao == 18:
    print('Está na hora de alistar-se combatente!')
elif ano - cidadao < 0:
    print('\33[31mDigitou o ano errado, favor verificar.\33[m')
elif ano - cidadao > 70:
    print('\33[31mDigitou o ano errado, favor verificar.\33[m')
elif ano - cidadao > 18:
    print('Passou do tempo de alistar-se, você está {} ano(s) atrasado!'.format(ano - cidadao - 18))
else:
    print('Falta ainda {} ano(s) para se alistar.'.format((ano - cidadao - 18) * -1))


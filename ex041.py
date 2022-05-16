"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:
- Até 9 anos : MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER"""

# Importação de bibliotecas
from datetime import date

# Cores
vermelho = '\33[31m'
fechamento = '\33[m'

# Captura o ano de nascimento
ano_nadador = int(input('Digite o ano de nascimento: '))

# Captura ano do Computador
ano = date.today().year

# Calcula idade do nadador
idade = ano - ano_nadador

# Avalia e dá relatório.

if idade <= 9:
    print('Sua idade é {}. Sua categoria é {}MIRIM{}!'.format(idade, vermelho, fechamento))
elif idade > 9 and idade <= 14:
    print('Sua idade é {}. Sua categoria é {}INFANTIL{}!'.format(idade, vermelho, fechamento))
elif idade > 14 and idade <= 19:
    print('Sua idade é {}. Sua categoria é {}JUNIOR{}!'.format(idade, vermelho, fechamento))
elif idade >19 and idade <=20:
    print('Sua idade é {}. Sua categoria é {}SENIOR{}!'. format(idade, vermelho, fechamento))
else:
    print('Sua idade é {}. Sua categoria é {}MASTER{}!'.format(idade, vermelho, fechamento))

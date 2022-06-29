""" Crie um programa que leia: nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar."""

# Importação de bibliotecas
from datetime import date


# Cadastra o trabalhador em um dicionário.
trabalhador = {'nome': str(input('Nome: ')).strip().upper(),
               'idade': date.today().year - int(input('Ano de nascimento: ')),
               'ctps': int(input('Nº CTPS (0 se não tem): '))}

# Laço de repetição verificando se foi preeichida a informação da CTPS.
if trabalhador['ctps'] == 0:  # Caso não tem cadastrada CTPS, não gera somente informações de nome e idade.
    print('-=' * 30)
    for t, v in trabalhador.items():
        print(f'- {t} tem valor {v}.')
else:  # Caso gere informações de CTPS, além das info acima, vai gerar ano contratação, salário e idade aposentadoria.
    trabalhador['ano_contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário em R$: '))
    trabalhador['aposentadoria'] = (trabalhador['ano_contratação']+35)-(date.today().year - trabalhador['idade'])
    print('-=' * 30)
    for t, v in trabalhador.items():
        print(f'- {t} tem valor {v}.')

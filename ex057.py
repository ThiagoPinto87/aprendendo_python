""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' OU 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

# Forma do professor Guanabara.

sexo = str(input('Sexo [F/M]: ')).strip().upper()

while sexo not in 'MmFm':
    print('Informação inválida. \33[31mPor favor, digite "F" ou "M"\33[m.')
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
if sexo == "F":
    print('O sexo digitado foi {}.'.format('FEMININO'))
else:
    print('O sexo digitado foi {}.'.format('MASCULINO'))




"""# Minha forma de resolver o problema.
# Gostei mais da forma do professor Guanabara que coloca a string do laço de forma mais profissional.
sexo = str(input('Sexo [F/M]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Informação inválida. \33[31mPor favor, digite "F" ou "M"\33[m.')
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
if sexo == "F":
    print('O sexo digitado foi {}.'.format('FEMININO'))
else:
    print('O sexo digitado foi {}.'.format('MASCULINO'))"""

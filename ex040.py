"""Crie um programa que leia duas notas de um alino e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

# Captura as notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Avalia a média
media = (nota1 + nota2) / 2

# Imprime o relatório
if media < 5:
    print('Sua média foi de {:.2f}. Você está REPROVADO!'.format(media))
elif 5 <= media < 7:
    print('Sua média é de {:.2f}. Você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é de {:.2f}. Você está APROVADO. Parabéns!!!'.format(media))
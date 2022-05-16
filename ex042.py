"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero:  todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno:  todos os lados diferentes"""

# Para resolver este exercício temos que trabalhar com 3 avaliações: Faz a conta. Forma triangulo? Verificar que tipo.

# Cores
vermelho = '\33[31m'
verde = '\33[32m'
amarelo = '\33[33m'
fechamento = '\33[m'


print('-=' * 20)
print(('Analisador de Triângulos'))
print('-=' * 20)
r1 = float(input('Digite o tamanho do primeiro seguimento de reta: '))
r2 = float(input('Digite o tamonho do segundo seguimento de reta: '))
r3 = float(input('Digite o tamanho do terceiro seguimento de reta: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima {}PODEM FORMAR{} triângulos.'.format(amarelo, fechamento), end='')
    if r1 == r2 == r3:
        print('E esse triangulo será {}Equilátero{}.'.format(verde, fechamento))
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('E esse triangulo será {}Isósceles{}.'.format(verde, fechamento))
    elif r1 != r2 != r3:
        print('E esse triangulo será {}Escaleno{}.'.format(verde, fechamento))
else:
    print('Os seguimentos acima {}NÃO PODEM FORMAR{} triângulos.'.format(vermelho, fechamento))

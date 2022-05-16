""" NÃO CONSEGUI RESOLVER O PROBLEMA SOZINHO, ACHEI A FORMULA, PORÉM NÃO CONSEGUI IMPLEMENTAR A LÓGICA.
# TIVE QUE ASSISTIR A AULA."""


# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.

print('-=' * 20)
print(('Analisador de Triângulos'))
print('-=' * 20)
r1 = float(input('Digite o tamanho do primeiro seguimento de reta: '))
r2 = float(input('Digite o tamonho do segundo seguimento de reta: '))
r3 = float(input('Digite o tamanho do terceiro seguimento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulos.')
else:
    print('Os seguimentos acime NÃO PODEM FORMAR triângulos.')




"""
# Captura o tamanho dos 3 seguimentos de retas.

reta_1 = float(input('Digite o tamanho do primeiro seguimento de reta: '))
reta_2 = float(input('Digite o tamonho do segundo seguimento de reta: '))
reta_3 = float(input('Digite o tamanho do terceiro seguimento de reta: '))

# Cria uma lista ordenada entre os resultados.
lista = ([reta_1, reta_2, reta_3])
print(sorted(lista))

# Retorna os 3 lados do triângulo.
lado_a = (lista[0])
lado_b = (lista[1])
lado_c = (lista[2])

print('Lado A :', lado_a)
print('Lado B :', lado_b)
print('Lado C :', lado_c)

# Compara se a soma dos dois lados menores é maior que o último seguimento.
if (lado_a + lado_b) > lado_c:
    print('Os seguimentos de retas digitados formam um triângulo.')
else:
    print('Os seguimentos de retas digitados NÃO formam um triângulo.')
"""
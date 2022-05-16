""" Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

# Captura o número ao qual será feita a tabuada.
n1 = int(input('Digite um número inteiro: '))

# Monta a estrutura da tabuada e faz o calculo.
for numeral in range(0, 10 + 1, 1):
    print('{} x {:2} = {:2}'.format(n1, numeral, numeral * n1))

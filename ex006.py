#Crie um algoritmo que leia um número e mostre o seu dobro, o tríplo e raiz quadrada.
n1 = float(input('Digite um número:'))
d = n1 * 2
t = n1 * 3
raiz = n1 ** (1/2)
print('Os resultados de dobro, triplo e raiz quadrada de {} são:\nDobro: {};\nTriplo: {};\nRaiz quadrada:{:.2f}.'
      .format(n1, d, t, raiz))

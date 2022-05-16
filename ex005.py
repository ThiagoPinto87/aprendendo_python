#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número:'))
ant = n1 - 1
suc = n1 + 1

#Calculo
print('O número antecessor de {} é o {} e o sucessor é {}!'.format(n1, ant, suc))

#Outra forma de ser feito o calculo, visto que o programa é simples e não necessita de ser criado variáveis. Isso economiza memória no computador.
print('O número antecessor de {} é o {} e o sucessor é {}!'.format(n1, (n1-1), (n1+1)))

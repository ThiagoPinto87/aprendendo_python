""" Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso Ideal
- De 25 até 30: Sobrepeso
- De 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida.
"""
# Cores
vermelho = '\33[31m'
amarelo = '\33[33m'
fechamento = '\33[m'
# Captura o peso do indivíduo.
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

# Calcula o IMC
imc = peso / altura ** 2

# Imprime o relatório;
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está em seu peso ideal. Parabéns!!!')
elif imc < 30:
    print('Atenção, você está com sobrepeso. {}Cuidado{}!'.format(amarelo, fechamento))
elif imc <= 40:
    print('{}Cuidado{}, você está com obesidade!!!'.format(amarelo, fechamento))
else:
    print('{}Urgente, você está com obesidade mórbida. Procure um médico.{}'.format(vermelho, fechamento))

# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

# Mais outra forma de fazer é com o if simplificado e utilizando o mesmo objeto "preço" para imprimir no resultado.
dist = float(input('Digite a distancia da sua viagem: '))
preço = dist * 0.45 if dist > 200 else dist * 0.50
print('O preço da passagem é R${:.2f}'.format(preço))


"""
# Outra forma de resolver que usa o mesmo objeto "preço"
dist = float(input('Digite a distancia da sua viagem: '))
if dist > 200:
    preço = dist * 0.45
else:
    preço = dist * 0.50

print('O preço da passagem é R${:.2f}'.format(preço))
"""
#######################

'''
# Forma que encontrei para resolver o problema. (Com bastante floreio).
# Captura a distância percorrida da viagem.
dist = float(input('Qual a distância da sua viagem em Km? '))

# Cadastra o preço por Km.
tx_curt = 0.50
tx_long = 0.45

# Calcula o preço da passagem.
print('Seja bem vindo passageiro!')
print('Sua distancia registrada é de {}Km!'.format(dist))

if dist <= 200:
    # Calculo passagem curta
    preço_curta = dist * tx_curt
    print('O preço da passagem é de R${:.2f}!'.format(preço_curta))
else:
    # Calculo passagem longa
    preço_longa = dist * tx_long
    print('O preço da passgem é de R${:.2f}!'.format(preço_longa))'''

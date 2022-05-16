# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km/h acima do limite.


# Captura a velocidade do carro
vel_carro = float(input('Digite a velocidade do carro: '))

# Cadastros
vel_permitida = float(80)
tx_multa = float(7)

# Analisa se possui multa.

if vel_carro <= vel_permitida:
    print('-' * 33)
    print('Velocidade registrada de {}km/h'.format(vel_carro))
    print('Boa viagem!!!')
    print('-' * 33)
else:
    print('=' * 60)
    print('>' * 21, ' MULTADO!!! ', '<' * 21)
    print('Sua velocidade registrada foi de {}Km/h.'.format(vel_carro))
    print('Velocidade permitida da via é de {}Km/h.'.format(vel_permitida))
    # Calcula o valor da multa
    multa = (vel_carro-vel_permitida) * tx_multa
    print('Você pagará o valor de R${:.2f} pela infração cometida!!!'.format(multa))
    print('=' * 60)

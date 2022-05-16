""" Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos."""

# Captura os valores de primeiro termo e de razão.
prim_termo = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão: '))
# Aglutinador de de termos zerados e iniciais.
qtd_termos = 1
total = 0
mais = 10
# Laço de repetição com flag de parada
while mais != 0:
    # Contador de controle de quantidade de termos para aparecer.
    total = total + mais
    # Laço de repetição dentro de outro laço, com flag de parada conforme total de termos a serem demonstrados.
    while qtd_termos <= total:
        # Imprime desde o primeiro termo.
        print('{}'.format(prim_termo), end=' -> ')
        # Calcula os termos da PA.
        prim_termo = prim_termo + razao
        # Controlador de termos.
        qtd_termos += 1
    print('PAUSA')
    # Solicita ao usuário se ele quer mais termos.
    mais = int(input('Quantos termos vc quer  ostrar a mais?'))
# Imprime o relatório final.
print('Progressão finalizada com {} termos mostrados'.format(total))

"""
# Forma que eu fiz.
# Captura informação para primeiro termo e razão (passo).
prim_termo = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão: '))
qtd_termos = 1

# Laço de repetição da flag de parada.
while qtd_termos != 0:
    # Solicita quantos termos o usuário que ver.
    qtd_termos_usuario = int(input('Quantos termos quer ver?'))
    # Continua a Progressão Aritmética (PA) à partir de onde parou.
    qtd_termos_usuario = qtd_termos_usuario + qtd_termos
    # Laço de repetição da quantidade de termos escolhida pelo usuário.
    while qtd_termos < qtd_termos_usuario:
        # Fórmula da PA.
        pa = prim_termo + qtd_termos * razao
        #Contador de termos.
        qtd_termos += 1
        print('{}'.format(pa), end=' -> ')

print('Acabou')"""

""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""

# Solicita os dois valores:
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
menu = 0
# Abre o menu para o usuário informando caso escolha o número 5, ele encerrará o programa.
while menu != 5:
    menu = int(input('''Qual operação deseja realizar?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    
    Digite a opção: '''))

    # Aplica a operação somar.
    if menu == 1:
        print('\n')
        print('A soma dos dois números é {}.'.format(num1 + num2))
        print('\n')

    # Aplica a operação multiplicar
    elif menu == 2:
        print('\n')
        print('O produto dos dois números é {}.'.format(num1 * num2))
        print('\n')

    # Aplica a operação encontrar maior valor:
    elif menu == 3:
        print('\n')
        print('O maior número é {}.'.format(max(num1, num2)))
        print('\n')
    # Aplica a operação de troca de algum valor:
    elif menu == 4:
        menu4 = float(input('''Qual valor deseja trocar?
        [4.1] 1º valor
        [4.2] 2º valor
        Digite  a opção: '''))
        print('\n')
        # Laço para possível valor inválido.
        while menu4 != 4.1 and menu4 != 4.2:
            print('\33[31mInformação inválida! Por favor, tente novamente.\33[m')
            print('\n')
            menu4 = float(input('''Qual valor deseja trocar?
                    [4.1] 1º valor
                    [4.2] 2º valor
                    Digite a opção: '''))
            print('\n')
        # Altera o 1º valor.
        if menu4 == 4.1:
            num1 = int(input('Digite o 1º valor: '))
            print('\n')
            print('Atualização do 1º valor para: {}'.format(num1))
            print('\n')

        # Altera o 2º valor.
        else:
            num2 = int(input('Digite o 2º valor: '))
            print('\n')
            print('Atualização do 2º valor para: {}'.format(num2))
            print('\n')
# Finaliza o programa.
print('\n')
print('\33[33mOk, obrigado! Até mais\33[m')






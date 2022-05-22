""" Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta."""

# Para resolver essa questão, o programa deverá identificar e contar quantos parenteses tem abrindo e fechando e eles
# tem que ter a mesma quantidade.

expressao = str(input('Digite sua expressão: '))
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está ERRADA.')

""" Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while."""

prim_termo = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão: '))
qtd_termos = 1

while qtd_termos <= 10:
    print('{}'.format(prim_termo), end=' -> ')
    prim_termo = prim_termo + razao
    qtd_termos += 1

print('Acabou')


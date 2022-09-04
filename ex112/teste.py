""" Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetarios."""

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

valor = dado.leia_dinheiro('Digite um valor R$')
moeda.moeda_resumo(valor, 20, 12)


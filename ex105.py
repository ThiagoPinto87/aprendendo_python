"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguntes funções:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional)
Adicione também as docstrings da função."""


def notas(*nota, situacao=False):
    """
    Recebe as informações de notas e caso deseje analisa a situação do aluno.
    :param nota: Recebe as notas (pode ser quantas quiser).
    :param situacao: [Opcional] Caso parâmetro True, analisa se o aluno está Aprovado, Recuperação ou Reprovado.
    :return: Retorna informações de quantidade de notas lidas, a maior nota lida, a menor nota lida e a média das notas.
    """
    result = dict()
    result['qtd'] = len(nota)
    result['maior'] = max(nota)
    result['menor'] = min(nota)
    result['media'] = sum(nota) / len(nota)
    if situacao:
        if result['media'] >= 7:
            result['situacao'] = 'Aprovado'
        elif result['media'] >= 6:
            result['situacao'] = 'Recuperação'
        else:
            result['situacao'] = 'REPROVADO'
    return result


# Programa Principal
ficha = notas(5, 5.5, 8, 7, situacao=True)
print(ficha)
help(notas)

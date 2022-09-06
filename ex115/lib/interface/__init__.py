def leia_int(msg):
    while True:
        try:
            resultado = int(input(msg))
        except Exception as erro:
            print('\33[1:31mErro! Por favor, digite um número válido.\33[m')
            print(f'\33[1:33mO erro refere-se a {erro.__class__}.\33[m')
        else:
            return resultado


def linha(lin=42):
    print('_' * lin)


def margem(mar=42):
    print('=' * mar)


def cabeçalho_ajustavel(txt):
    margem(len(txt)+4)
    print(txt.center(len(txt)+4))
    margem(len(txt)+4)


def cabeçalho(txt):
    margem()
    print(txt.center(42))
    margem()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    print('Digite o número da opção desejada.'.center(42))
    c = 1
    for item in lista:
        print(f'\33[33m{c} -\33[m \33[34m{item}\33[m')
        c += 1
    margem()
    opc = leia_int('\33[32mSua opção: \33[m')
    return opc
    linha()


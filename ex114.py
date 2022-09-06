""" Crie um código em python que teste se o site pudim está acessível pelo computador usado."""

import urllib.request

while True:
    try:
        site = urllib.request.urlopen('http://pudim.com.br/')
    except:
        print('\33[1;31mO site NÃO está no ar.\33[m')
        break
    else:
        print(f'\33[1;33mO site está no ar.\33[m')
        break





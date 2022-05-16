# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

# Captura a temperatura em ºC.
celsius = float(input('Qual a temperatura em ºC?'))

# Converte ºC em ºF.
conversor = (celsius * 9/5) + 32

# Imprime o relatório.
print('A temperatura está em {:.1f}ºFahrenheit'.format(conversor))
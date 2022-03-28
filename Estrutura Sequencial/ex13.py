"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
"""
s = int(input("insira seu sexo (1 para masculino, 2 para feminino):"))
h = float(input("insira sua altura:")) * 100
if s == 1:
    peso = (72.2 * h) / 100 - 58
    print(f'peso ideal:', peso)
elif s == 2:
    peso = (62.2 * h) / 100 - 44.7
    print(f'peso ideal:', peso)

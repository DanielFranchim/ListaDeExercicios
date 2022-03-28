"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
n1 = int(input('Insira o primeiro Numero Inteiro:'))
n2 = int(input('Insira o segundo Numero Inteiro:'))
n3 = float(input('Insira o primeiro Numero Real:'))
a = (2 * n1) * (n2 / 2)
b = (3 * n1) + n3
c = n3 ** 3
print(f'a: {a}, b: {b}, c: {c}')

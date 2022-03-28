"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9). """
f = int(input('Temperatura em Fahrenheit:'))
c = 5 * (f - 32) / 1.8
print('Em graus Celsius', c)

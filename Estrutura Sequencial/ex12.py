"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58 """
altura = float(input("insira sua altura:")) * 100
peso = (altura / 100) * 72.7 - 58
print('seu peso ideal é:', peso)

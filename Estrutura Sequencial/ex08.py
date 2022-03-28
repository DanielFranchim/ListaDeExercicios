"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
ganho_hora = int(input('Ganho por Hora:'))
horas_mes = int(input('Horas Trabalhadas por Mês:'))
ganho_mes = ganho_hora * horas_mes
print('Voce ganho por mês R$', ganho_mes)

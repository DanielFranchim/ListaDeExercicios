"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
gph = int(input('Ganho por Hora:'))
htm = int(input('Horas Trabalhadas por Mês:'))
sal_b = gph * htm
ir = sal_b * 0.11
inss = sal_b * 0.08
sindicato = sal_b * 0.05
sal_l = sal_b - ir - inss - sindicato
print('+ Salário Bruto : R$', sal_b)
print('- IR : R$', ir)
print('+ Inss : R$', inss)
print('+ Sindicato : R$', sindicato)
print('+ Salário Liquido : R$', sal_l)

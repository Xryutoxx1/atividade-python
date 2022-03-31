#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao  INSS. quanto #pagou ao sindicato. o salário líquido.

ganho_hora = float(input('digite quanto você ganha por hora'))
hora_mes = float(input('quantas horas você trabalha ao mês '))


imposto_renda = ((ganho_hora*hora_mes)*11)/100
INSS = ((ganho_hora*hora_mes)*8)/100
sindicato = ((ganho_hora*hora_mes)*5)/100

print('seu salário total é de {:.2f}, descontando {:.2f} do imposto {:.2f} do INSS e {:.2f} do sindicato fica {:.2f}'.format(ganho_hora*hora_mes,imposto_renda,INSS,sindicato, (ganho_hora*hora_mes)-imposto_renda - INSS - sindicato ))
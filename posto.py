#Um posto está vendendo combustíveis com a seguinte tabela de descontos: Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Álcool: 
#até 20 litros, desconto de 3% por litro 
#acima de 20 litros, desconto de 5% por litro 
#     b) Gasolina: 
#até 20 litros, desconto de 4% por litro 
#acima de 20 litros, desconto de 6% por litro 

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

escolha_cliente = input('deseja colocar Alcool ou Gasolina? ')

if escolha_cliente == 'Alcool' or 'alcool':
    quantidade = int(input('qual a quantidade em Litro?'))
    if quantidade  <=20:
        quantidade = (quantidade*1.90)
        desconto = (quantidade/100)*3
        print('você irá pagar o total de ${:.2f} Reais'.format(quantidade - desconto))
    else:
        quantidade = (quantidade*1.90)
        desconto = (quantidade/100)*5
        print('você irá pagar o total de ${:.2f} Reais'.format(quantidade - desconto))

elif escolha_cliente == 'Gasolina' or 'gasolina':
    quantidade = int(input('qual a quantidade em Litro?'))
    if quantidade <=20:
        quantidade = (quantidade*2.50)
        desconto = (quantidade/100)*4
        print('você irá pagar o total de ${:.2f} Reais'.format(quantidade - desconto))
    else:
        quantidade = (quantidade*2.50)
        desconto = (quantidade/100)*6
        print('você irá pagar o total de ${:.2f} Reais'.format(quantidade-desconto))
else:
    print('não entendi oque você digitou! Porfavor tente novamente.')


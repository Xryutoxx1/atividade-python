#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total. 

metros_pintar = int(input('quantos metros você deseja pintar? '))
tinta = 54 #quantidade que a lata pinta
lata = 1
custo = 80
if tinta < metros_pintar:
    while tinta < metros_pintar:
        tinta = tinta+54
        lata = lata+1
        custo = custo+80
else:
    print('com {} latas, você consegue pintar {} metros, gastando {} Reais.'.format(lata,metros_pintar,custo))
print('com {} latas, você consegue pintar {} metros, gastando {} Reais.'.format(lata,metros_pintar,custo))
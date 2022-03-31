#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos e segundos).

arquivo_tamanho = float(input('digite o tamanho do arquivo'))
velocidade_internet = float(input('digite a velocidade da internet em Mbps'))
tempo_segundos = 1


taxa_transferencia_seg = velocidade_internet/8

if taxa_transferencia_seg < arquivo_tamanho:
    while taxa_transferencia_seg < arquivo_tamanho:
        taxa_transferencia_seg = taxa_transferencia_seg+ taxa_transferencia_seg
        tempo_segundos = tempo_segundos +1
    print('seu dowload irá demorar {} segundos'.format(tempo_segundos))

else:
    print('seu Dowload irá demorar 1 segundo!')
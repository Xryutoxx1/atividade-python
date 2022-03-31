#faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são:
#"Telefonou para a vítima?" 
#"Esteve no local do crime?" 
#"Mora perto da vítima?" 
#"Devia para a vítima?" 
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('1 para sim e 0 para não.')
telefone = int(input('Telefonou para a vítima?'))
local = int(input('Esteve no local do crime?'))
moradia = int(input('Mora perto da vítima?'))
devendo = int(input('Devia para a vítima?'))
trabalho = int(input('Já trabalhou para a vítima?'))

resposta = telefone + local + moradia + devendo + trabalho

if resposta == (2):
    print('você é um suspeito.')
elif resposta == (3):
    print('você é um cúmplice')
elif resposta == (4):
     print('você é um cúmplice')
elif resposta == (5):
    print('você é o assasino. Está preso!')
elif resposta == (0):
    print('inocente.')
elif resposta == (1):
    print('inocente.')
else:
    print('não compreendo oque você quer dizer.')

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('digita sua nota'))
nota2 = float(input('digite sua nota'))
media = (nota1+nota2)/2

if media >=7 and media <=9:
    print('Aprovado')
elif media == 10:
    print('Aprovado com distinção!')
elif media>10:
    print('tá mentindo a nota safado')
elif media < -1:
    print('ta doido kkkkk')

else:
    print('Reprovado')
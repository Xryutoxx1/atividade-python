from random import randint
numero = randint(0,10)
x = 0
pergunta = int(input('tente adivinhar o número escolhido pela maquina: '))

while pergunta != numero:
    pergunta = int(input('Errou! tente novamente: '))
    x= x+1
print('acertou!! você fez um total de {} tentativas e a resposta é {}'.format(x, numero))

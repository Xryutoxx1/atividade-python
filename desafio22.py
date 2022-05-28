peso = []
pergunta = ()
for c in range(0,5):
    pergunta = int(input('digite o peso'))
    peso.append(pergunta)
print('a pessoa com o peso de {} é a mais leve já a pessoa com o peso {} é a mais pesada.'.format(min(peso),max(peso)))
tabuada = int(input('digite um numero para ver sua tabuada'))
resposta = []
x = 0
for c in range(0, 11):
    x = tabuada*c
    resposta.append(x)
print(resposta)

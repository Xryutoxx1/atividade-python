lista = []
x = 0
peg1 = int(input('digite um número'))
lista.append(peg1)
peg2 = int(input('digite um número'))
lista.append(peg2)

maior = max(lista)
menor = min(lista)

while True:
    maior = maior - 1
    if maior <= menor:
        break
    x = x + maior
    print(maior)
print(x)

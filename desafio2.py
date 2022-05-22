# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem
base = int(input('digite um número'))
expoente = int(input('digite um número'))
lista = []
resultado = 0

while True:
    expoente = expoente - 1
    if expoente == 0:
        break
    lista.append(expoente)
print(lista)



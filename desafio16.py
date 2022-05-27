num_int = 0
par = []
soma = 0


for c in range(0, 6):
    num_int = int(input('digite um numero'))
    if num_int % 2 == 0:
        soma = soma + num_int
        par.append(soma)

print(soma)

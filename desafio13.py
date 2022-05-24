
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []
impar = []
for x in range(0, len(numeros)):
    if numeros[x] % 2 == 0:
        par.append(numeros[x])
    else:
        impar.append(numeros[x])
        
print(f'>par:{par} \n>impar:{impar}')
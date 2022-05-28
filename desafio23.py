somaidade = 0
nomehomemvelho = 0
idadehomemvelho = ''
mulheridade = 0 
for c in range(1, 5):
    print('---- {} PESSOA ----'.format(c))
    nome = str(input('digite o nome: '))
    idade = int(input('digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade 
    
    #somando a quantidade de mulheres com menos de 20
    if sexo in 'Ff' and idade <20:
        mulheridade = mulheridade+1
    
    
    #descobrindo o nome do homem mais velho
    elif c == 1 and  sexo in 'Mm':
        nomehomemvelho = nome
        idadehomemvelho = idade
    
    elif sexo in 'Mm':
        if idade > idadehomemvelho:
            nomehomemvelho = nome
            idadehomemvelho = idade


print('a méida da idade é de {:.1f}'.format(somaidade/4))
print('o homem mais velho se chama {}'.format(nomehomemvelho))
print('o total de mulheres com menos de 20 anos é de {}'.format(mulheridade))

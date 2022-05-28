data = ()
pergunta =  ()
for c in range(0, 7):
    pergunta = int(input('digite o ano de nascimento: '))
    data = 2022 - pergunta
    if data >= 21:
        print('é de maior!')
    else:
        print("é de menor!")
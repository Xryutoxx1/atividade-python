nome = 'l'
while len(nome) < 3:
    nome = str(input('digite um nome maior que 3 letras: '))
idade = -1
while idade < 0 or idade > 150:
    idade = int(input('digite sua idade: '))
salario = 0
while salario <= 0:
    salario = float(input('Digite o seu salário: '))
estadocivi = 'a'
while estadocivi in 'abefghijklmnopqrtuvwxyz':
    estadocivi = str(
        input('digite seu estado civil S/C/V/D: '))
sexo = 'a'
while sexo in 'abcdeghijklnopqrstuvwxyz':
    sexo = str(input('digite seu sexo M/F: '))

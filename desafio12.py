
while True:
    login = '1'
    senha = '1'
    if login == senha:
        while True:
            login = str(input('digite o login: '))
            senha = str(input('digite sua senha: '))
            if login != senha:
                break
    break

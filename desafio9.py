a = int(input('digite número A: '))
b = int(input('digite o número B: '))
x = 0
if a >= b:
    while a >= b:
        taxacrescia = a/100
        taxacrescib = b/100
        a = a + taxacrescia*1
        b = b + taxacrescib*3
        x = x+1
        print(x)

if b >= a:
    while b >= a:
        taxacrescia = a/100
        taxacrescib = b/100
        a = a + taxacrescia*3
        b = b + taxacrescib*1
        x = x+1
        print(x)

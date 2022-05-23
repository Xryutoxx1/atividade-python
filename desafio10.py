a = 80000
b = 200000
x = 0

while b >= a:

    taxacrescia = a/100
    taxacrescib = b/100
    a = a + taxacrescia*3
    b = b + taxacrescib*1.5
    x = x+1
    print(x)

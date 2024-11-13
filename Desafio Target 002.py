n = int(input('Digite um numero para saber se ele pertence a seguencia de fibonacci: '))
f1 = 0
f2 = 1
if n == f1 or n == f2:
    print(f'O numero {n} pertence a sequencia fibonacci')
else:
    f = 0
    while f < n:
        f = f1 + f2
        f1 = f2
        f2 = f

    print(f'O numero {n} pertence a seguencia de fibonacci' if f == n else f'O numero {n} não pertence a sequencia de fibonachi')
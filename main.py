def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

def is_in_fibonnaci(n):
    i = 1
    while fibonnaci(i) <= n:
        if fibonnaci(i) == n:
            return True
        i += 1
    return False

n = int(input('Digite um numero: '))
if is_in_fibonnaci(n):
    print(f'O numero {n} pertence a sequencia de fibonnaci')
else:
    print(f'O numero {n} nao pertence a sequencia de fibonnaci')
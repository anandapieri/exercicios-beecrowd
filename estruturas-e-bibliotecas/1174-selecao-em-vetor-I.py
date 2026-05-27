numeros = []

for _ in range(100):
    A = float(input())
    numeros.append(A)

for indice, valor in enumerate(numeros):
    if valor <= 10:
        print(f'A[{indice}] = {valor:.1f}')

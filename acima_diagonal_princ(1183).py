def calculo_na_matriz(operacao: str, matriz: list):
    soma = sum(matriz)
    if operacao == 'S':
        print(f'{soma:.1f}')
    elif operacao == 'M':
        print(f'{soma/66:.1f}')

operacao = input()

matriz = []
c = 1
for i in range(12):
    linha_matriz = []
    for j in range(12):
        N = float(input())
        linha_matriz.append(N)
    matriz.extend(linha_matriz[c:])
    c += 1

calculo_na_matriz(operacao, matriz)

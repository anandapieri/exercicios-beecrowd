def calculo_na_matriz(linha: int, operacao: str, matriz: list):
    if operacao == 'S':
        soma = sum(matriz[linha])
        print(soma)
    elif operacao == 'M':
        media = sum(matriz[linha])/12
        print(media)

linha = int(input())
operacao = input()

matriz = []
linha_matriz = []
for i in range(12):
    for j in range(12):
        N = float(input())
        linha_matriz.append(N)
        if len(linha_matriz) == 12:
            matriz.append(linha_matriz)
            linha_matriz = []

calculo_na_matriz(linha, operacao, matriz)

''' for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)'''
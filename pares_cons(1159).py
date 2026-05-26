i = 1
resultados = []
while i != 0:
    i = int(input())
    if i % 2 == 0:
        soma = 5*i + 20
        resultados.append(soma)
    else:
        soma = 5*i + 25
        resultados.append(soma)

del(resultados[-1])

for item in resultados:
    print(item)
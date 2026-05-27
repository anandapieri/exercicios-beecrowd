N = int(input())
input() #consome uma linha da entrada, eh como se fosse quebra de linha | "Você está usando input() para avançar o cursor de leitura do arquivo de entrada"

for caso in range(N):
    especies = {}
    i = 0
    while True:
        try:
            especie = input()
        except EOFError:
            break

        if especie == '':
            break
        
        i += 1
        if especie in especies:    #especies[nome] = especies.get(nome, 0) + 1
            especies[especie] += 1
        else:
            especies[especie] = 1
    
    for key, value in sorted(especies.items()):
        print(f'{key} {(value/i)*100:.4f}')

    if caso != N - 1:  #não imprime linha em branco após o último caso
        print()
    


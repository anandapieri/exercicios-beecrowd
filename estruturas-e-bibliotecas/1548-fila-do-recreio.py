N = int(input())

for _ in range(N):
    M = int(input())
    ordem = list(map(int, input().split()))
    ordem_decrescente = sorted(ordem, reverse=True)
    contador = 0
    for i in range(M):
        if ordem[i] == ordem_decrescente[i]:
            contador += 1
    print(contador)
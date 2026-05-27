N = int(input())

for _ in range(N):
    texto = input().split()
    for palavra in texto:
        print(palavra[0], end='')
    print()
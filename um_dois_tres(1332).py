N = int(input())

for _ in range(N):
    palavra = input().strip()

    if len(palavra) == 5:
        print(3)
    else:
        acertos = (
            (palavra[0] == 'o') +
            (palavra[1] == 'n') +
            (palavra[2] == 'e')
        )

        if acertos >= 2:
            print(1)
        else:
            print(2)
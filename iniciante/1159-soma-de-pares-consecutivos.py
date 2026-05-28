while True:
    X = int(input())
    if X == 0:
        break
    elif X % 2 == 0:
        soma = 5*X + 20
        print(soma)
    else:
        soma = 5*X + 25
        print(soma)
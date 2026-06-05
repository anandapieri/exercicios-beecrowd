while True:
    N = input()

    if N == '0':
        break

    jogadas = input().split()
    print(f"Mary won {jogadas.count('0')} times and John won {jogadas.count('1')} times")
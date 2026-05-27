leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

N = int(input())
for _ in range(N):
    V = input()
    i = 0
    for digito in V:
        i += leds.get(digito)
    print(f'{i} leds')
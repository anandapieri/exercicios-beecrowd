numero = int(input())

print(f'N[0] = {numero}')

for V in range(1,10):
    i = numero*2
    print(f'N[{V}] = {i}')
    numero = i

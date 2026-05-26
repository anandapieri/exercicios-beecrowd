N = int(input())

i = 0
o = 0
for numero in range(N):
    X = int(input())
    if X in range(10, 21):
        i+=1
    else:
        o+=1

print(f'{i} in\n{o} out')

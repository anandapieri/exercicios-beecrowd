N = int(input())

C = []
R = []
S = []
i = 0

for _ in range(N):
    tipo = input().split()
    if tipo[1] == 'C':
        C.append(int(tipo[0]))
    elif tipo[1] == 'R':
        R.append(int(tipo[0]))
    else:
        S.append(int(tipo[0]))
    i += int(tipo[0])

total_coelhos = sum(C)
total_ratos = sum(R)
total_sapos = sum(S)

print(f'Total: {i} cobaias')
print(f'Total de coelhos: {total_coelhos}\nTotal de ratos: {total_ratos}\nTotal de sapos: {total_sapos}')
print(
    f'Percentual de coelhos: {(total_coelhos/i)*100:.2f} %\n'
    f'Percentual de ratos: {(total_ratos/i)*100:.2f} %\n'
    f'Percentual de sapos: {(total_sapos/i)*100:.2f} %'
)
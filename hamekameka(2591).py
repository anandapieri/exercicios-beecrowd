C = int(input())

for _ in range(C):
    ataque = input()
    posicao_1o_m = ataque.find('m')
    posicao_2o_m = ataque.find('m', posicao_1o_m + 1)
    ataque_final = 'k' + 'a' * (posicao_1o_m - 1) * (posicao_2o_m - (posicao_1o_m + 3))
    print(ataque_final)
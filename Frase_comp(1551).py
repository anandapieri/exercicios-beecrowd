def verificador_de_frase(frase:str):
    sem_repetidos = ''.join(set(frase))
    alfabeto = [(chr(numero)) for numero in range(97, 123)]
    l = 0
    for letra in sem_repetidos:
        if letra in alfabeto:
            l +=1
    return l

N = int(input())
i = 0
qnt_de_l = []
while i < N:
    frase = input()
    verificacao = verificador_de_frase(frase)
    qnt_de_l.append(verificacao)
    i+=1

for item in qnt_de_l:
    if item == 26:
        print('frase completa')
    elif 13 <= item < 26:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
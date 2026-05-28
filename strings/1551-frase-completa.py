def verificador_de_frase(frase:str):
    sem_repetidos = ''.join(set(frase))
    alfabeto = [(chr(numero)) for numero in range(97, 123)]
    l = 0
    for letra in sem_repetidos:
        if letra in alfabeto:
            l +=1
    return l

testes = int(input())

for _ in range(testes):
    frase = input()
    verificacao = verificador_de_frase(frase)
    
    if verificacao == 26:
        print('frase completa')
    elif 13 <= verificacao < 26:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
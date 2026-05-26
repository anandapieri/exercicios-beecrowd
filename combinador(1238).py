def combinador(palavra1: str, palavra2: str):
    tamanho_minimo = min(len(palavra1), len(palavra2))
    combinador = ''
    for i in range(tamanho_minimo): 
        combinador += palavra1[i]
        combinador += palavra2[i]
    combinador += palavra1[tamanho_minimo:]
    combinador += palavra2[tamanho_minimo:]  
    return combinador

N = int(input())
for _ in range(N):
    palavra1, palavra2 = (input().split())
    print(combinador(palavra1, palavra2))
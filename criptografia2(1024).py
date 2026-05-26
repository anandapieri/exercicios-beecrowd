N = int(input())

for _ in range(N):
    texto = input()

    texto_criptografado_1 = ''
    for caracter in texto:
        if caracter.isalpha():
            texto_criptografado_1 += chr(ord(caracter) + 3)
        else:
            texto_criptografado_1 +=caracter

    texto_criptografado_2 = texto_criptografado_1[::-1] #inversão da linha

    N = len(texto_criptografado_2)//2
    
    texto_criptografado_final = texto_criptografado_2[:N]

    for caracter in texto_criptografado_2[N:]:
        texto_criptografado_final += chr(ord(caracter) - 1)

    print(texto_criptografado_final)
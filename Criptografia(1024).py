def criptografar(texto: str):
    #1a regra
    texto_criptografado = []
    for simbolo in texto:
        if simbolo.isalpha():
            X = chr(ord(simbolo)+3)
            texto_criptografado.append(X)
        else:
            texto_criptografado.append(simbolo)

    #2a regra
    texto_concatenado = ''.join(texto_criptografado[::-1])

    #3a regra:
    texto_criptografado_3 = []
    meio = len(texto_concatenado) // 2
    primeira_parte = texto_concatenado[:meio]
    segunda_parte = texto_concatenado[meio:]
    texto_criptografado_3.append(primeira_parte)
    for item in segunda_parte:
        Y = chr(ord(item)-1)
        texto_criptografado_3.append(Y)

    criptografia_final = ''.join(texto_criptografado_3[::])

    return criptografia_final
    
N = int(input())
i = 0
textos_crip = []
while i < N:
    M = input()
    criptografia = criptografar(M)
    textos_crip.append(criptografia)
    i+=1
    
for _ in textos_crip:
    print(_)


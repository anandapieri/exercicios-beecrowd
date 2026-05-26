def mensagem_oculta(palavra:str):
    for item in palavra:
        mensagem = [item[0] for item in palavra]
        mensagem_final = ''.join(mensagem[::])
    return mensagem_final

i = 0
mensagens = []
N = int(input())
while i < N:
    palavra = input().split()
    M = mensagem_oculta(palavra)
    mensagens.append(M)
    i+=1

for item in mensagens:
    print(item)
def formata_vetor(lista: list, nome: str):
    for indice, valor in enumerate(lista):
        print(f'{nome}[{indice}] = {valor}')

par = []
impar = []

for _ in range(15):
    numero = int(input())

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    
    if len(par) == 5:
        formata_vetor(par, 'par')
        par = []
    elif len(impar) == 5:
        formata_vetor(impar, 'impar')
        impar = []

if impar:
    formata_vetor(impar, 'impar')
if par:
    formata_vetor(par, 'par')
def formata_vetor_par(par: list):
    for indice, valor in enumerate(par):
        print(f'par[{indice}] = {valor}')

def formata_vetor_impar(impar: list):
    for indice, valor in enumerate(impar):
        print(f'impar[{indice}] = {valor}')

par = []
impar = []

for _ in range(15):
    numero = int(input())

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    
    if len(par) == 5:
        formata_vetor_par(par)
        par = []
    elif len(impar) == 5:
        formata_vetor_impar(impar)
        impar = []

if impar:
    formata_vetor_impar(impar)
if par:
    formata_vetor_par(par)
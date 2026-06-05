N = int(input())

numeros_pares = []
numeros_impares = []

for _ in range(N):
    numero = int(input())
    
    (numeros_pares.append(numero)) if (numero % 2 == 0) else (numeros_impares.append(numero))


for numero_par in sorted((numeros_pares)):
    print(numero_par)

for numero_impar in sorted((numeros_impares), reverse=True):
    print(numero_impar)
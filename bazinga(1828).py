def rodar_jogo(sheldon, raj):
    regras = {'pedra': ['lagarto', 'tesoura'], 
            'tesoura': ['papel', 'lagarto'], 
            'papel': ['pedra', 'Spock'],
            'lagarto': ['Spock', 'papel'], 
            'Spock': ['tesoura', 'pedra']}

    if sheldon == raj:
        return ('De novo!')
    elif raj in regras[sheldon]: #verifica se o valor de "raj" está/pertence a chave "sheldon"
        return ('Bazinga!')
    else:
        return('Raj trapaceou!')

testes = int(input())
i = 0
partidas = []
while i < testes:
    jogada = input().split()
    sheldon = jogada[0]
    raj = jogada[1]
    resultado = rodar_jogo(sheldon, raj)
    partidas.append(resultado)
    i+=1

for i, resultado in enumerate(partidas, start=1):
    print(f'Caso #{i}: {resultado}')
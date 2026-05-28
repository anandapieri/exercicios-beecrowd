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
for i in range(testes):
    jogada = input().split()
    sheldon = jogada[0]
    raj = jogada[1]
    resultado = rodar_jogo(sheldon, raj)
    print(f'Caso #{i+1}: {resultado}')
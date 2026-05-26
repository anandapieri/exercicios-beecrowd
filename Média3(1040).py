def calcular_media(N1, N2, N3, N4):
    media = (N1*2+N2*3+N3*4+N4)/10
    print(f'Media: {media:.1f}')
    if media >= 7:
        print('Aluno aprovado.')
    elif media < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        exame = float(input())
        print(f'Nota do exame: {exame}')
        media_final = (exame + media)/2
        print('Aluno aprovado.') if media_final >= 5 else print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')

nota = input().split()
N1 = float(nota[0])
N2 = float(nota[1])
N3 = float(nota[2])
N4 = float(nota[3])
calcular_media(N1, N2, N3, N4)
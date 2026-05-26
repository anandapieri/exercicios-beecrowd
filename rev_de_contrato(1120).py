while True:
    D, N = input().split()
    digitos = []

    if D =='0' and N =='0':
        break
    else: 
        for digito in N:
            if digito == D:
                continue
            else:
                digitos.append(digito)

    todos_0 = all(x == digitos[0] for x in digitos)

    if not digitos: #lista vazia
        print('0')
    elif len(digitos) != 1 and todos_0: #todos os elementos 0 
        print('0')
    else:
        print(''.join(digitos))
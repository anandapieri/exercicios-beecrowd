while True:
    try:
        texto = input().split()

        qnt = 0
        tamanho = 0
        for palavra in texto:
            if palavra.isalpha():
                qnt+=1
                tamanho += len(palavra)
            elif palavra.endswith('.') and palavra[:-1].isalpha():
                qnt+=1
                tamanho += len(palavra[:-1])

        try:
            media = tamanho/qnt
            if media < 4:
                print(250)
            elif 4 <= media < 6:
                print(500)
            else:
                print(1000)
        except ZeroDivisionError:
            print(250)
            
    except EOFError:
        break
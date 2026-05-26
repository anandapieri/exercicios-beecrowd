while True:
    try:
        expressao = input()

        i = 0
        for caracter in expressao:
            if caracter == '(':
                i += 1
            elif caracter == ')':
                i -= 1
                if i < 0:
                    break
        if i == 0:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break
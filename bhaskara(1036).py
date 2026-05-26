def raizes_bhaskara(A: float, B: float, C: float):
    delta = B ** 2 - 4*A*C
    if delta < 0:
        print('Impossivel calcular')
    else:
        try:
            raiz_delta = delta ** 0.5
            R1 = (-B + raiz_delta)/(2*A)
            R2 = (-B - raiz_delta)/(2*A)
            print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')
        except ZeroDivisionError:
            print('Impossivel calcular')

A, B, C = map(float, input().split())
raizes_bhaskara(A, B, C)
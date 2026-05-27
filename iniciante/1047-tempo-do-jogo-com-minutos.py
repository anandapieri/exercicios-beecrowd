hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

tempo_inicial_em_min = 60*hora_inicial + minuto_inicial
tempo_final_em_min = 60*hora_final + minuto_final

if tempo_final_em_min > tempo_inicial_em_min:
    tempo_total_em_min = tempo_final_em_min - tempo_inicial_em_min
    hora_jogo = tempo_total_em_min // 60
    minuto_jogo = tempo_total_em_min % 60
    print(f'O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)')
else:
    tempo_final_em_min += 24*60
    tempo_total_em_min = tempo_final_em_min - tempo_inicial_em_min
    hora_jogo = tempo_total_em_min // 60
    minuto_jogo = tempo_total_em_min % 60
    print(f'O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)')

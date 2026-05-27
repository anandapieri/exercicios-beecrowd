cidade_num = 1

while True:
    N = int(input())
    if N == 0:
        break

    consumo_por_media = {}
    total_moradores = 0
    total_consumo = 0

    for _ in range(N):
        moradores, consumo = map(int, input().split())

        media = consumo // moradores #chave de consumo_por_media

        if media not in consumo_por_media:
            consumo_por_media[media] = moradores #adição pela chave | valor: moradores
        else:
            consumo_por_media[media] += moradores

        total_moradores += moradores
        total_consumo += consumo

    print(f"Cidade# {cidade_num}:")

    for media in sorted(consumo_por_media):
        print(f"{consumo_por_media[media]}-{media}", end=" ")

    print() #quebra de linha
    consumo_medio_geral = total_consumo / total_moradores
    print(f"Consumo medio: {consumo_medio_geral:.2f} m3.")

    cidade_num += 1
    print() #quebra de linha

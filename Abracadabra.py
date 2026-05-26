import sys

palavras = sys.stdin.read().splitlines()

for i, palavra in enumerate(palavras):

    for j in range(len(palavra)):
        print(" " * j + " ".join(palavra[:len(palavra) - j]))

    # imprime linha em branco APENAS se não for o último caso
    if i != len(palavras) - 1:
        print()
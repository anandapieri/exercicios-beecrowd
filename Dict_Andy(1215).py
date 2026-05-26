import re
import sys

def listar_palavras(texto: str):
    partes = re.split(r'[^a-zA-Z]+', texto)
    return [palavra.lower() for palavra in partes if palavra]

palavras_dicionario = set ()

for linha in sys.stdin:                    # Lê até EOF de forma eficiente
    palavras = listar_palavras(linha)
    palavras_dicionario.update(palavras)

for palavra in sorted(palavras_dicionario):
    print(palavra)
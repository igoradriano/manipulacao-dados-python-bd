import os

try:
    os.rmdir("meu_diretorio2")
    print("Diretório Removido!")
except FileNotFoundError as erro:
    print("Diretório inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para criar o diretório")
    print("Descrição", erro)
except OSError as erro:
    print("Outro erro.")
    print(" O diretório está vazio?")
    print("Descrição", erro)

print("Término do programa")

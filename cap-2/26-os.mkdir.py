import os

try:
    os.mkdir("meu_diretorio2")
    print("Diretório Criado!")
except FileExistsError as erro:
    print("Diretório já existente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para criar o diretório")
    print("Descrição", erro)

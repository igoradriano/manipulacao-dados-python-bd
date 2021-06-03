import os

try:
    os.replace("teste.txt","teste.renomeado.txt")
    print("Arquivo sobrescrito!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Arquivo destino já existe")
    print("Descrição", erro)

    
print(" Término do Programa!")

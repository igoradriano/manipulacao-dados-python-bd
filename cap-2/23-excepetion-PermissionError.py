print("Abrindo um arquivo")

try:
    arquivo = open("teste.txt", "w")
    print("Arquivo aberto")
    arquivo.write("Conteúdo da primeira linha.")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)

print("Término do Programa")
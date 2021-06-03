def extrair_linha(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        #print(arquivo.readlines())
        return arquivo.readlines()[0] #READLINES LÊ O ARQUIVO INTEIRO E NESTE CASO RETORNA APENAS O PRIMEIRO TERMO DO ARRAY GERADO ; coloque o return comentado e acine o print para ver


primeira_linha = extrair_linha("dados.txt")
print(primeira_linha)
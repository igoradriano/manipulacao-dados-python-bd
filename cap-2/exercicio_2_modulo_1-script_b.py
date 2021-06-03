def extrair_linha(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        linhas = arquivo.readlines()  #LE O CONTEUDO INTEIRO E COLOCA CADA LINHA DENTRO DE UM ARRAY
        for linha in linhas:  #PERCORRE TODOS OS INDICES D ARRAY
            #print(linha)
            return linha #RETORNA O PRIMEIRO TERMO (COLOQUE O RETURN COMENTADO E VEJA O PRINT)



primeira_linha = extrair_linha("dados.txt")
print(primeira_linha)
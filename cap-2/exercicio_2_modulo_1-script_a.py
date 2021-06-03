def extrair_linha(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        linhas = arquivo.read() #LÊ TUDO COMO UMA STRING ÚNICA
        for linha in linhas: #LOGO LINHA SE REFERE A UMA LETRA DA FRASE TODA LINHAS
            return linha #RETORNA A PRMEIRA LETRA



primeira_linha = extrair_linha("dados.txt")
print(primeira_linha)

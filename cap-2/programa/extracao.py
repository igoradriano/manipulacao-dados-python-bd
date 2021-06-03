# coding: utf-8
import principal
import pandas as pd

variaveis = principal.extrair_variaveis("dados/dicionario_pessoas.xls")

colunas = [str(variavel) for variavel in variaveis]  # codigo - descricao ,codigo-descricao, codigo-descricao...
linhas = []
with open("dados/pessoas_2015.txt") as microdados:
    for idx, linha in enumerate(microdados):
        print("++++++++++++++++++++++ NOVA LINHA +++++++++++++++++++++++")
        nova_linha = []
        for variavel in variaveis:
            print(variavel)
            print(variavel.categoria)
            # vamos da posicao inicial ate a posicao inicial + tamanho --> linha[1:6]
            valor = linha[variavel.posicao_inicial:variavel.posicao_inicial + variavel.tamanho].strip()
            if valor:
                valor = int(valor)
            print('\t', valor, ' - ', variavel.categoria.get(valor))
            valor_final = variavel.categoria.get(valor) if variavel.categoria.get(valor) else valor
            nova_linha.append(valor_final)
        linhas.append(nova_linha)
        if idx > 100:
            break
df = pd.DataFrame(linhas, columns=colunas)
print(df.shape) #356904 linhas e 434 colunas
df.to_csv("microdados.csv", sep=";")  #mais de 2GB
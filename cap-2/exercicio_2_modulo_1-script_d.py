def extrair_linha(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        for linha in arquivo: #NESTE CASO COMO PASSAMOS DIRETAMENTE O ARQUIVO PARA O ITERAVEL
            #print(linha)  #PODEMOS VERIFICAR ISSO COM O PRINT
            return linha  #ELE IRÁ lÊ SOMENTE A PRIMEIRA LINHA MESMO
            


primeira_linha = extrair_linha("dados.txt")
print(primeira_linha)


#PODERIAMOS TER UTILIZADO O MÉTODO ITERÁVEL READLINE()

def extrair_linha2(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        return arquivo.readline() #NESTE CASO COMO PASSAMOS DIRETAMENTE O ARQUIVO PARA O ITERAVEL


primeira_linha2 = extrair_linha2("dados.txt")
print(primeira_linha2)
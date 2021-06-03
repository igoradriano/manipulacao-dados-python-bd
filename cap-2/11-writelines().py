linhas = ["Conteúdo da primeira linha.",
          "\nConteúdo da segunda linha.",
          "\nConteúdo da terceira linha",
          "\nConteúdo da Quarta linha"]

arquivo_escrita = open("dados_writelines.txt", "w")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

arquivo_escrita =open("dados_writelines.txt","r")
print(arquivo_escrita.read())
arquivo_escrita.close()

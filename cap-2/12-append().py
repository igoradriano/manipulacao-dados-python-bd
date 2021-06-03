arquivo_escrita = open("dados_write.txt", "a")

arquivo_escrita.write("\nConteúdo adicional.Cada vez que executamos uma nova linha é adicionada")

arquivo_escrita.close()
arquivo_escrita = open("dados_write.txt","r")
print(arquivo_escrita.read())
arquivo_escrita.close()
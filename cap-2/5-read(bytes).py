arquivo = open("dados.txt", "r")

conteudo = arquivo.read()

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo retornado pelo read:")
print(repr(conteudo)) #representa um objeto como uma única string
print((conteudo))  #imprime as linhas do arquivo da maneira como aparecem no arquivo

arquivo.close()

arquivo = open("dados.txt", "r")
conteudo = arquivo.read(5) # para ler somente 3 bytes
print(repr(conteudo)) #representa um objeto como uma única string
print((conteudo))  #imprime as linhas do arquivo da maneira como aparecem no arquivo


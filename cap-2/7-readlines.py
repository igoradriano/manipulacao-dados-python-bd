arquivo = open("dados.txt", "r")

conteudo = arquivo.readlines()

print("Tipo do conteúdo:", type(conteudo)) #eja que esse tipo é uma lista e não string

print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))
print((conteudo))

arquivo.close()

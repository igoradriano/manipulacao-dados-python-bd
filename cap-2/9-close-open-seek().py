arquivo = open("dados.txt", "r")

conteudo = arquivo.read()
print("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura), '\n')

arquivo.close()

#FECHAMOS E REABRIMOS O ARQUIVO PARA PODER O CURSOS SE POSICIONAR NO INICIO NOVAMENTE
arquivo_reaberto = open("dados.txt", "r")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')


# ATRAVÉS DO SEEK() CONSEGUIMOS POSICIONAR O CURSOR NA LINHA DESEJADA PARA NÃO UTILIZAR O CLOSE() -> OPEN()
arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo_reaberto.close()

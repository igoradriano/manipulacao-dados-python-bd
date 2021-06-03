import psycopg2 as conector

# Criando uma conexão e um cursor
conexao = conector.connect(database='Aula4Python', user='postgres', password='051094', host='127.0.0.1', port='5432')
cursor = conexao.cursor()
print("conexão estabelecida com sucesso")

# Primeiro comando no Banco
cursor.execute("""SELECT * FROM "AGENDA" WHERE "id"=1""")
registro = cursor.fetchall()
print(registro)

# Segundo comando no Banco = Atualização de um único registro
cursor.execute("""UPDATE "AGENDA" SET "telefone"='9298138043' WHERE "id"=1""")
#commitando os 2 comandos anteriores
conexao.commit()
print("registro atualizado com sucesso")

# Terceiro comando no Banco- Resgatando novos valores
cursor.execute("""SELECT * FROM "AGENDA" WHERE "id"=1""")
registro = cursor.fetchall()
print(registro)
conexao.commit()
print("registro resgatado com sucesso")

conexao.close()
print("conecao fechada com sucesso")



#

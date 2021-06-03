import psycopg2 as ps

# Criando a conexão com o postgres
conexao = ps.connect(database='Aula4Python', user='postgres', password='051094', host='127.0.0.1', port='5432')
print("conexão criada com sucesso")

# Criando o cursor
cursor = conexao.cursor()
print("cursor criado com sucesso")

# Gerando a requisição no banco
cursor.execute("""INSERT INTO "AGENDA"("id","nome","telefone") VALUES(1,'pessoa 1', '92988560409');""")
print("comando executado com sucesso")
#No caso do banco de dados PostgreSQL, o nome da tabela e dos campos deve estar entre aspas duplas, por causa
# disso é que o comando insert possui três aspas duplas logo no início e no final. Sendo assim, muita atenção
# com isso, pois existem algumas variações conforme o sistema gerenciador de banco de dados escolhido.

# Commitando o estado do banco
conexao.commit()
print("estado do banco commitado com sucesso")

#Fechando a conexão e o cursor
cursor.close()
conexao.close()
print("conexao e cursor com o banco fechados com sucesso")
#------------------------------------------------------------------------------------------------
import psycopg2 as conector
from faker import Faker
#------------------------------------------------------------------------------------------------
conexao = conector.connect(database = "Aula4Python",
                            user="postgres",
                            password="051094",
                            host="127.0.0.1",
                            port="5432")
print("Conexão aberta com sucesso")

cursor = conexao.cursor()
print("Cursor criado com sucesso")
fake = Faker("pt-BR")
#------------------------------------------------------------------------------------------------
n = 10
for i in range(10):
    codigo = i+1000
    nome = f'produto {i+1}'
    preco = fake.pyfloat(left_digits=3,
                        right_digits=2,
                        positive=True,
                        min_value=80000,
                        max_value = 200000)
    print(preco)
    print(nome)

    comando_sql = """ INSERT INTO "PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES(%s,%s,%s)"""
    registro = (codigo, nome, preco)
    cursor.execute(comando_sql, registro)
#------------------------------------------------------------------------------------------------
conexao.commit()
print("Inserção realizado com sucesso!")
conexao.close()
print("Conexão com o Postgres fechada!")
#------------------------------------------------------------------------------------------------


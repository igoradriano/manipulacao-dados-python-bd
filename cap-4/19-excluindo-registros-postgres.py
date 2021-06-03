import psycopg2 as conector

conexao = conector.connect(database='Aula4Python', user='postgres', password='051094', host='127.0.0.1', port='5432')

cursor = conexao.cursor()

cursor.execute("""DELETE FROM "AGENDA" WHERE "nome" ='teste 1' """)

conexao.commit()

cont = cursor.rowcount

print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!")
conexao.close()
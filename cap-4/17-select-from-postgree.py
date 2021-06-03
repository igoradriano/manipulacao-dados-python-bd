import psycopg2 as conector

conexao = conector.connect(database='Aula4Python', user='postgres', password='051094', host='127.0.0.1', port='5432')

cursor = conexao.cursor()

cursor.execute("""SELECT * FROM "AGENDA" where "id"=1 """)

#registro = cursor.fetchone()
registro2 = cursor.fetchall()

#print(registro)
print(registro2)

conexao.commit()
print("Seleção realizada com sucesso!")

cursor.close()
conexao.close()
print("conexão fechada com sucesso")

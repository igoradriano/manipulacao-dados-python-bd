import psycopg2

con = psycopg2.connect(database='postgres', user='postgres', password='051094', host = "127.0.0.1", port = "5432")
print("Conexão com o PostGress Aberta com sucesso!")
cursor = con.cursor()
cursor.execute('''CREATE TABLE Agenda(
                    id int primary key not null,
                    Nome text not null,
                    Telefone char(12));''')
print('Tabela criada com sucesso!')
con.commit()
cursor.close()
con.close()
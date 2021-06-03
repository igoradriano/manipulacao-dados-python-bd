import sqlite3 as conector
#import mysql.connector as conector
#import psycopg2 as conector

try:
    #Abertura de uma coneção
    conexao = conector.connect("./meu_banco.db")

    #Aquisição de um cursor:
    cursor = conexao.cursor()

    #Execução de comando: SELECT... CREATE...
    comando = '''CREATE TABLE Marca(
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla NOT NULL,
                    PRIMARY KEY (id)
                    );'''
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de banco de dados",err)

finally:
    # Fechamento das conexões e cursores
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão e cursor encerrados com sucesso!")

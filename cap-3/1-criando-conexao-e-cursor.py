import sqlite3 as conector
#import mysql.connector as conector
#import psycopg2 as conector

#Abertura de uma coneção
conexao = conector.connect("URL SQLite")

#Aquisição de um cursor:
cursor = conexao.cursor()

#Execução de comando: SELECT... CREATE...
cursor.execute("...")
cursor.fetchall()

#Efetivação do comando
conexao.commit()

#Fechamento das conexões
cursor.close()
conexao.close()

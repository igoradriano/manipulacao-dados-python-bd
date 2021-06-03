import sqlite3 as conector
from ModeloQueries import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()


comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando,{"usa_oculos": True})

registros = cursor.fetchall()

for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf: ", type(registro),"-----------", "Conteúdo: ", pessoa.cpf)
    print("nome: ", type(registro),"-----------", "Conteúdo: ", pessoa.nome)
    print("nascimento: ", type(registro),"-----------", "Conteúdo: ", pessoa.data_nascimento)
    print("oculos: ", type(registro),"-----------", "Conteúdo: ", pessoa.usa_oculos)

if conexao:
    cursor.close()
    conexao.close()
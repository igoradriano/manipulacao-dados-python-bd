import sqlite3 as conector
from ModeloQueries import Pessoa

conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES) #Isso indica que o conector deve tentar fazer uma conversão dos dados, tomando como base o tipo da coluna declarada no CREATE TABLE.
cursor = conexao.cursor()

#Funções conversores:
def conv_bool(dado):
    return True if dado == 1 else False

# Registro de conversores:
conector.register_converter("BOOLEAN", conv_bool)

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
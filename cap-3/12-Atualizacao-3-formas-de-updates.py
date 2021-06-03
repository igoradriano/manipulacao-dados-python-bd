import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# ATUALIZE TODAS AS PESSOAS PARA OCULOS = 1
comando1 = '''UPDATE Pessoa SET oculos=1;'''
cursor.execute(comando1)

# ATUALIZE PARA USE OCULOS = FALSE(0), ONDE O CPF FOR 98712284220 
comando2 = ''' UPDATE Pessoa SET oculos=? WHERE cpf=98712284220; '''
cursor.execute(comando2, (False,))

# ATUALIZE PARA USE OCULOS = FALSE(0) ONDE O CPF FOR 61846350263
comando3 = ''' UPDATE Pessoa SET oculos = :usa_oculos WHERE cpf = :cpf;'''
cursor.execute(comando3, {"usa_oculos": False, "cpf":61846350263})

conexao.commit()

if conexao:
    cursor.close()
    conexao.close()
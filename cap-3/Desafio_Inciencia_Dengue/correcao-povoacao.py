import sqlite3 as conector

try:
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()
    print("Conexao estabelecida")


    comando = '''UPDATE Populacao SET ano = 2019 WHERE ano=2018;'''
    cursor.execute(comando)
    print("Comando Executado com sucesso")
    conexao.commit()
    print("Commit realizado com sucesso")

except conector.OperationalError as err:
    print("Erro Operacional", err)
except conector.IntegrityError as err:
    print("Erro de integridade", err)
except conector.DatabaseError as err:
    print("Erro do Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexao fechada com sucesso")
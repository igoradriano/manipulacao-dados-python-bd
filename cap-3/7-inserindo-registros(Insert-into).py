import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Conexão e cursor estabelecidos com sucesso")

    comando = ''' INSERT INTO Pessoa( cpf,nome,nascimento,oculos)
            VALUES (61846350263, 'Carolina','1978-06-07',1);'''
    cursor.execute(comando)
    print("Comando executado com sucesso")

    conexao.commit()
    print("Conexão commitada com sucesso")

except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Cursor e Conexão finalizados com sucesso")
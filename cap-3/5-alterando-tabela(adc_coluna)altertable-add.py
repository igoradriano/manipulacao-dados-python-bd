import sqlite3 as conector
try:
    # Adicionando conexão e cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Conexão criada com sucesso")

    # Atribuindo comando para aleterar a tabela e adicionar uma coluna
    comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''
    print("Comando criado com sucesso")

    # Executando o comando
    cursor.execute(comando)
    print("Comando executado com sucesso")
    # Commitando a conexão
    conexao.commit()
    print("Comando commitado com sucesso")

except conector.DatabaseError as err:
    print("Erro no Banco de Dados", err)
finally:
    if conexao:
        # Fechando a conexão e cursor
        cursor.close()
        conexao.close()
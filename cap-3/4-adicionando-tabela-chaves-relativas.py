import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Execução de um comando: SELECT...
    comando = '''CREATE TABLE Veiculo(
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''
    cursor.execute(comando)
    print("Tabela criada com sucesso!")

    # Efetivação do comando
    conexao.commit()
    print("Commit realizado com sucesso!")
except conector.DatabaseError as err:
    print("Erro de Banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão encerrada com sucesso!")

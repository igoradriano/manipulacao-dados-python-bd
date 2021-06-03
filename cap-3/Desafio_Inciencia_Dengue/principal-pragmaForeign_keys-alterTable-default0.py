import sqlite3 as conector


conexao = None
cursor = None
try:
    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on") # Para habilitar a restrição de chave estrangeira:
    cursor = conexao.cursor()
    print("Banco de Dados criado com sucesso...")
#Para impor o relacionamento entre as linhas na tabela1 e tabela2, você usa as restrições de chave estrangeira .
#Isso evita que quando excluirmos uma linha da tabela1 fiquem linhas orfãs na tabela2.

    comando = '''CREATE TABLE Municipio(
                    codigo INTEGER NOT NULL,
                    nome VARCHAR(32) NOT NULL,
                    PRIMARY KEY(codigo)
                    );'''
    cursor.execute(comando)
    print("Tabela Municipio criada com sucesso")

    comando = '''CREATE TABLE Populacao(
                    codigo INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    PRIMARY KEY(codigo, ano),
                    FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                    );'''
    cursor.execute(comando)
    print("Tabela Populacao criada com sucesso")

    comando = '''CREATE TABLE Dengue(
                    codigo INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    casos INTEGER NOT NULL,
                    PRIMARY KEY(codigo, ano),
                    FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                    );'''
    cursor.execute(comando)
    print("Tabela Dengue criada com sucesso")

    comando = '''ALTER TABLE Populacao
                    ADD populacao INTEGER DEFAULT 0 NOT NULL;'''
    cursor.execute(comando)
    # Devemos colocar um DEFAULT 0 para setar que todos os valores que já estavam presentes no banco não sejam nulos
    # e sim recebam zero

    conexao.commit()
    print("Conexão commitada com sucesso")

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    # Fechamento das conexões e cursores
    if cursor:
        cursor.close()
        conexao.commit()
        print("Cursor e Conexão Fechado com sucesso!")


# Se quisermos criar um banco de dados em memória, que será criado para toda execução do programa,
# basta utilizar o comando
# conexao = sqlite3.connect(':memory:')
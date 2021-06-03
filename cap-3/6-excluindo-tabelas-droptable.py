'''OBS: Precisamos colocar as colunas em ordem, porém Como nem todos os bancos de dados, incluindo
 o SQLite, dão suporte à criação de colunas em posição determinada, vamos precisar remover nossa tabela para
 recriá-la com os atributos na posição desejada. '''

import sqlite3 as conector
try:
    # Estabelecendo Conexão e cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Conexão e Cursor estabelecidos com sucesso")

    # Executando Comandos
    comando1 = ''' DROP TABLE Veiculo;'''
    cursor.execute(comando1)
    print("Comando1 executado com sucesso")

    comando2 = '''CREATE TABLE Veiculo(
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''
    cursor.execute(comando2)
    print("Comando2 executado com sucesso")

    # Commitando conexão
    conexao.commit()
    print("Conexão commitada com sucesso")

except conector.DatabaseError as err:
    print("Erro no Banco de Dados", err)

finally:
    # Fechando Conexão e cursor
    if conexao:
        cursor.close()
        conexao.close()
        print("Cursor e conexão fechados com sucesso")
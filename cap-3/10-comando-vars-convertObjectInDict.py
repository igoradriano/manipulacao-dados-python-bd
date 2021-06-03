import sqlite3 as conector
from ModeloQueries import Pessoa

try:
    # Estabelecendo uma conexão e um cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Conexão estabelecida com sucesso")

    # Instanciando Objeto do tipo pessoa
    pessoa = Pessoa(77944458120,"Earle","1974-10-02",0)
    print("Instacia de Objeto do tipo pessoa criada com sucesso")

    # Definindo os Comandos SqLite
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) 
        VALUES (:cpf,:nome, :data_nascimento, :usa_oculos);'''
    # OBS: NOTE QUE INDEPENDENTE DA ORDEM DOS PARÂMETROS DENTRO DO OBJETO, ELE CONSEGUIRÁ IDENTIFICAR OS PARÂMETROS
    #NA ORDEM CORRETA COM O MÉTODO INTERNO "vars()".
    cursor.execute(comando, vars(pessoa))
    print("Comandos definidos com sucesso")

    # Validando a mudanço no BD
    conexao.commit()
    print("Commit realizado com sucesso")

# Tratando execeções
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
except conector.OperationalError as err:
    print("Erro Operacional", err)

# Finalizando o Programa
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Cursor e Conexão fechados com suscesso")
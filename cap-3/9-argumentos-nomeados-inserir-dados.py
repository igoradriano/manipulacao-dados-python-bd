import sqlite3 as conector
from ModeloQueries import Pessoa

try:
    # Estabelecendo uma conexão e um cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Conexão e cursor estabelecidos com sucesso")

    # Criando uma instancia do tipo Pessoa
    pessoa = Pessoa(14788525892, "Ayumi","1987-10-22",True)
    print("Instancia do tipo pessoa criada com sucesso")

    # Definindo os comandos SQlite
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) 
            VALUES (:cpf,:nome, :data_nascimento, :usa_oculos);'''

    # Note que não precisamos passar os parâmetros em ordem dentro do dicionário
    cursor.execute(comando,{"nome":pessoa.nome,
                            "cpf":pessoa.cpf,
                            "data_nascimento":pessoa.data_nascimento,
                            "usa_oculos":pessoa.usa_oculos})
    print("Comando Executado com sucesso")

    # Commitando (validando) o novo Estado do Banco de Dados
    conexao.commit()
    print("A conexão com o banco de Dados foi commitada com sucesso")

# Tratando as Exceções
except conector.DatabaseError as err:
    print("Erro no Banco de Dados", err)
except conector.OperationalError as err:
    print("Erro de Operação", err)

# Finalizando o Programa
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("O cursor e a conexão foram fechadas com sucesso")
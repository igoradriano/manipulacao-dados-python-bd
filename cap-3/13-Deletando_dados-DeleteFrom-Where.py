import sqlite3 as conector 

try:
    # Criando uma conexão e um cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    print("Cursor e Conexao criados com sucesso")

    # Deletando com uma string sem delimitador "?"
    comando = '''DELETE FROM Pessoa WHERE cpf=61846350263;'''
    cursor.execute(comando)
    print("Primeiro Comando Especificado com suscesso")

   # Deletando com uma string com argumentos nomeados
    comando1 = '''DELETE FROM Pessoa WHERE cpf=:cpf;'''
    cursor.execute(comando1,{"cpf":98712284220})
    print("Segundo Comando Especificado com suscesso")


    # Validando a alteração do DB
    conexao.commit()
    print("Conexao commitada com sucesso")

   # Tratamento de Exceções 
except conector.IntegrityError as err:
    print("Erro de Integridade", err)
except conector.DatabaseError as err:
    print("Erro do Banco de Dados", err)
except conector.OperationalError as err:
    print("Erro de Operação", err)

# Finalizando o programa
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Curso e conexao fechados com sucesso")
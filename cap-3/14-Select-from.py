import sqlite3 as conector

try:
    #Iniciando uma conexão e um cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Criando um comando
    comando = '''SELECT * FROM Pessoa;'''

    #Executando o comando
    cursor.execute(comando)

    # Recuperando os dados
    registros = cursor.fetchall()
    print("Tipo retornado pela fetchall:", type(registros))


     #SEM NECESSIDADE DE COMMIT!!


     
    for registro in registros:
        print("Tipo: ", type(registro), "Conteúdo: ", registro)

# Levantando exceções
except conector.IntegrityError as err:
    print("Erro de Integridade", err)
except conector.DatabaseError as err:
    print("Erro do Banco de Dados", err)
except conector.OperationalError as err:
    print("Erro de Operação", err)

finally: 
    #Fechando a conexao e o cursor
    if conexao:
        cursor.close()
        conexao.close()


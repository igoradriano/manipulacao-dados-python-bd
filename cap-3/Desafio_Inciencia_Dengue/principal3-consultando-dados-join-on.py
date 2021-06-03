import sqlite3 as conector

conexao = None
cursor = None
try:
    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_key = on")
    cursor=conexao.cursor()

    comando = '''SELECT Municipio.nome, Dengue.casos, Populacao.populacao 
                FROM Municipio
                JOIN Dengue ON Municipio.codigo = Dengue.codigo
                JOIN Populacao ON Municipio.codigo = Populacao.codigo
                WHERE Dengue.ano = :ano AND Populacao.ano = :ano'''

                
    ano = {"ano":2019}
    cursor.execute(comando, ano)

    # Recuperacao dos dados
    registros = cursor.fetchall()
    print(registros[0])
    print(f'{"municipio":30} - {"casos":5} - {"populacao":9} - {"incidencia":8} - {"%":6}')
    for registro in registros:
        incidencia = registro[1]/registro[2]   #casos/populacao
        inc_porcent = incidencia * 100
        print(f'{registro[0]:30} - {registro[1]:5} - {registro[2]:9} - {incidencia:.6f} - {inc_porcent:2.4f} %')
    
    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    if conexao:
        cursor.close()
        conexao.close()

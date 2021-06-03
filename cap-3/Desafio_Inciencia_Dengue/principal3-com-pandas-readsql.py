import sqlite3 as conector
import pandas as pd

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

                
    ano = {"ano":2020}
    cursor.execute(comando, ano)

    # Recuperacao dos dados
    resultado = pd.read_sql(sql=comando, con=conexao, params=ano)
    resultado['incidencia'] = 100 * resultado['casos']/resultado['populacao'] # criando nova coluna incidencia
    print(resultado)
    print(resultado['incidencia'].describe()) #imprime descricao da coluna incidencia
    #retorna o numero de linhas, media, desvio padrao, minimo, primeiro segundo e terceiro quartil, valor maximo observado
    print(resultado.loc[resultado['incidencia'].idxmax()]) # retorna todos os dados do maior valor de incidencia
    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    if conexao:
        cursor.close()
        conexao.close()

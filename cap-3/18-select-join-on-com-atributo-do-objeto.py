import sqlite3 as conector
from ModeloQueries import Veiculo, Marca

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()


comando = '''SELECT * FROM
                Veiculo JOIN Marca ON Marca.id=Veiculo.marca;'''

cursor.execute(comando)
registros = cursor.fetchall()

for registro in registros:
    print(registro)
    marca = Marca(*registro[7:]) # insere apenas os valores do indice 7 em diante, pois o JOIN foi feito assim: (veiculo.1, veiculo.2, veiculo.3, veiculo.4, veicul.5, veiculo.6, marca.7, marca.8, marca.9)
    veiculo = Veiculo(*registro[:5], marca)  # insere até o índice 5 dos valores do registro, o ultimo indice preenche com um objeto do tipo marca.
    print("Placa :", veiculo.placa, "Marca:", veiculo.marca.nome)



if conexao:
    cursor.close()
    conexao.close()
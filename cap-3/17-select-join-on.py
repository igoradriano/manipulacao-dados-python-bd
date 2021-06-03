import sqlite3 as conector
from ModeloQueries import Veiculo

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()


comando = '''SELECT 
                    Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario,
                    Marca.nome FROM Veiculo JOIN Marca ON (Marca.id = Veiculo.marca);'''

cursor.execute(comando)
registros = cursor.fetchall()

for registro in registros:
    veiculo = Veiculo(*registro)
    print("Placa: ", veiculo.placa, "Marcar: ", veiculo.marca)

cursor.execute(comando)
registros = cursor.fetchall()
for registro in registros:
    print(registro)


if conexao:
    cursor.close()
    conexao.close()
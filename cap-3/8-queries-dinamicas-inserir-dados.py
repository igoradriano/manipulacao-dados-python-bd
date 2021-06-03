import sqlite3 as conector
from ModeloQueries import Pessoa

# Abertura de conexao e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()
print("Conexão estabelecida com sucesso")

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(12387495682, 'Maximizer', '1990-10-23', False)
print("Instanciamento do Objeto realizado com sucesso")

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES(?,?,?,?);'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))
print("Comando executado com sucesso")

# Efetivação do comando
conexao.commit()
print("Conexão commitada com sucesso")

# Fechamento da Conexão
cursor.close()
conexao.close()
print("Conexão fechada com sucesso")
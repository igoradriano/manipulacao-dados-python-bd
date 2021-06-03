import sqlite3 as conector
from ModeloQueries import Marca, Veiculo

try:
    # Estabelecendo conexão e cursor com o BD
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")  # Criando restrição para chaves estrangeiras
    cursor = conexao.cursor()
    print("Conexão e cursor estabelecidos com sucesso")

    # Definindo comando 1
    comando = '''INSERT INTO Marca(nome, sigla) VALUES (:nome, :sigla);'''
    print("Primeiro Comando Epecificado")

    # Instanciando objeto do tipo marca, executando comando 1
    marca1 = Marca("Lamborghini", "LB")
    cursor.execute(comando,vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Ferrari", "FR")
    cursor.execute(comando, vars(marca2))
    marca2.id = cursor.lastrowid  #lastrowid ->  adiciona id automaticamente através do indice da ultima linha aprontado pelo cursor
    print("marcas adicionadas com sucesso")


    # Definindo comando 2
    comando2 = '''INSERT INTO Veiculo 
            VALUES(:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    #Note que não preciso especificar os campos de veículo, apenas inserir os valores em ordem



    # Instanciando objetos do tipo veículo
    veiculo1 = Veiculo("ABA0081", 2001, "Prata", 1.0, 98712284220, 1)
    veiculo2 = Veiculo("BBA0072", 2002, "Preto", 1.4, 61846350263, 1)
    veiculo3 = Veiculo("CBA0083", 2003, "Branco", 2.0, 98712284220, 2)
    veiculo4 = Veiculo("DBA0094", 2004, "Azul", 3.0, 98712284220, 2)
    print("Segundo Comando Epecificado")

    # Executando comandos
    cursor.execute(comando2,vars(veiculo1))
    cursor.execute(comando2,vars(veiculo2))
    cursor.execute(comando2,vars(veiculo3))
    cursor.execute(comando2,vars(veiculo4))
    print("Vaiculos adicionados com sucesso")

    # Validando Comandos
    conexao.commit()
    print("Commit realizado com sucesso")

   
# Tratamento de exceções 
except conector.IntegrityError as err:
    print("Erro de Integridade", err)
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
except conector.OperationalError as err:
    print("Erro operacional", err)


finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Cursor e conexão fechados com sucesso")


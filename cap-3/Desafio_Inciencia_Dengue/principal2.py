import sqlite3 as conector
from modelos import Dengue, Municipio, Populacao

try:
    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    print("Conexão e cursor estabelicidos com sucesso")


    with open('dengue_rj.csv') as arquivo:
        arquivo.readline()  # descarta o cabeçalho, quando executo o readline o cursos passa para linha de baixo
        for linha in arquivo:
            codigo, nome, casos_2019, casos_2020 = linha.strip().split(";")
            # strip retira espaços vazios, split(";") separa os dados quando encontrar ;
            print(codigo, nome, casos_2019, casos_2020)


            municipio = Municipio(codigo, nome)
            comando = '''INSERT INTO Municipio VALUES(:codigo, :nome);''' #parâmetros nomeados
            cursor.execute(comando, vars(municipio))  #utilizamos o vars pois todos os dados serao inseridos
        

            dengue_2019 = Dengue(codigo, 2019, int(casos_2019))
            dengue_2020 = Dengue(codigo, 2020, int(casos_2020))
            comando = '''INSERT INTO Dengue VALUES(:codigo,:ano,:casos);'''
            cursor.execute(comando,vars(dengue_2019))
            cursor.execute(comando,vars(dengue_2020))
        print("Municipio Povoado com sucesso")
        print("Dengue povoado com sucesso")
    arquivo.close()


    with open("populacao.csv") as arquivo:
        arquivo.readline()
        for linha in arquivo:
            codigo, nome, pop_2019, pop_2020 = linha.strip().split(";")
            print(codigo, nome, pop_2019, pop_2020)
            comando = '''INSERT INTO Populacao VALUES(?,?,?);'''  #delimitador ?
            #populacao1 = Populacao(codigo,2019,pop_2019)
            #populacao2= Populacao(codigo,2020,pop_2019)
            #comando = '''INSERT INTO Populacao VALUES(:codigo, :ano, :populacao);'''
            #cursor.execute(comando,{"coodigo":populacao1.codigo,"ano":populacao1.ano,"populacao":populacao1.populacao})
            #cursor.execute(comando,{"coodigo":populacao2.codigo,"ano":populacao2.ano,"populacao":populacao2.populacao})
            cursor.execute(comando, (codigo, 2019, pop_2019))
            cursor.execute(comando, (codigo, 2020, pop_2020))
        print("Populacao povoada com sucesso")
    arquivo.close()

     # validando Mudança de Estado do BD
    conexao.commit()
    print("Commit realizado com sucesso")

# Tratamento de Exceções
except conector.OperationalError as err:
    print("Erro Operacional, ", err)
except conector.IntegrityError as err:
    print("Erro de Integridade, ", err)
except conector.DatabaseError as err:
    print("Erro de Banco de Dados, ",err)

finally:
    if conexao:

        cursor.close()
        conexao.close()
        print("Cursor e Conexao finalizada com sucesso")








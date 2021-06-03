import psycopg2 as conector


class AppDB:
    def __init__(self):
        print("Método construtor!")

#---------------------------------------------------------------------------------------------------------
# Método para abrir conexão
#---------------------------------------------------------------------------------------------------------
    def abrirConexao(self):
        try:
            self.conexao = conector.connect(
                            database='Aula4Python',
                            user='postgres',
                            password='051094',
                            host='127.0.0.1',
                            port='5432')
            print("Conexao com o Banco estabelecida")
        except (Exception, conector.Error) as err:
            if self.conexao:
                print("Falha ao se conectar ao Banco de Dados", err)

#---------------------------------------------------------------------------------------------------------
# Método para selecionar dados
#---------------------------------------------------------------------------------------------------------
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.conexao.cursor()

            cursor.execute("""SELECT * FROM "PRODUTO" """)
            print("operação de seleção realizada com sucesso")
            registros = cursor.fetchall()
            print(registros)

        except (Exception, conector.Error) as err:
            print("Error in select operation", err)

        finally:
            if self.conexao:
                cursor.close()
                self.conexao.close()
                print(" A conexão com o Postgres foi fechada")
        return registros

#---------------------------------------------------------------------------------------------------------
# Método para inserir Dados
#---------------------------------------------------------------------------------------------------------
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.conexao.cursor()

            postgres_insert_query="""INSERT INTO "PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES(%s,%s,%s)"""
            record_to_insert = (codigo,nome, preco)
            cursor.execute(postgres_insert_query,record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, conector.Error) as err:
            if(self.conexao):
                print("Falha ao inserir registro na tabela PRODUTO", err)
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print(" A conexão com o Postgres foi fechada.")

#---------------------------------------------------------------------------------------------------------
# Método para atualiza dados
#---------------------------------------------------------------------------------------------------------
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.conexao.cursor()

            print("Registros antes da atualização")
            sql_select_query = """SELECT * FROM  "PRODUTO" WHERE "CODIGO" = %s """
            cursor.execute(sql_select_query,(codigo,))
            registros = cursor.fetchone()
            print(registros)

            # Atualizar registro
            sql_select_query = """UPDATE "PRODUTO" SET "NOME" = %s, "PRECO" = %s WHERE "CODIGO" = %s"""
            cursor.execute(sql_select_query,(nome, preco,codigo))
            self.conexao.commit()

            count= cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro Depois da Atualização")
            sql_select_query = """SELECT * FROM "PRODUTO" WHERE "CODIGO"=%s"""
            cursor.execute(sql_select_query, (codigo,))
            registros = cursor.fetchone()
            print(registros)

        except conector.Error as err:
            print("Erro na Atualização", err)
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print("A conexão com o Postgres foi fechada.")

#---------------------------------------------------------------------------------------------------------
# Método para excluir Dados
#---------------------------------------------------------------------------------------------------------
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.conexao.cursor()

            sql_delete_query = """DELETE FROM "PRODUTO" WHERE "CODIGO"=%s """
            cursor.execute(sql_delete_query, (codigo,))
            self.conexao.commit()

            count= cursor.rowcount
            print(count, "Registro excluido com sucesso!")
        except conector.Error as err:
            print("Erro na Exclusão", err)
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print("A conexão com o Postgres foi fechada.")

"""#---------------------------------------------------------------------------------------------------------
# Criando Registros e instanciando a Classe AppDB
#---------------------------------------------------------------------------------------------------------
lista = []
carros = ["Ferrari", "Lamborghini","Punto","Gol","Golf","HRV","CIVC","KWID","Sandero","Uno","Argo","T-cros","Virtus","Bugatti"]
i=500
for n in range(0,10):
    for carro in carros:
        i+=1
        if carro == "Ferrari" or carro == "Lamborghini" or carro=="Bugatti":
            lista.append((i,f'{carro} {n}', 1000000+n*10000))
        lista.append((i,f'{carro} {n}', 84800+n*100))


banco = AppDB()
for item in lista:
    banco.inserirDados(item[0],item[1],item[2])"""
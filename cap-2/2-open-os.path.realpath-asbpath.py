import os
import time
# Para o arquivo dados1.txt
arquivo1 = open("dados1.txt")  # Caminho relativo
arquivo2 = open(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\dados1.txt") # Caminho absoluto

# Para o arquivo dados2.txt
arquivo3 = open("documentos/dados2.txt")  # Caminho relativo
arquivo4 = open(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")  # Caminho absoluto
#UTILIZEI O "r" ANTES DO CAMINH ABSOLUTO PARA PODER CONVERTER UMA STRING NORMAL EM STRING BRUTA

print(os.path.relpath(arquivo1.name)) #is.path.relpath(path, start=os.curdir) -> star opcional e padrão curdir(diretório atual) ; Serve para retornar o caminho relativo.
print(os.path.abspath(arquivo1.name)) #os.path.abspath(paht) -> retorna o caminho absoluto
print(os.path.relpath(arquivo2.name))
print(os.path.abspath(arquivo3.name))
print(arquivo1)

#OUTROS MÉTODOS DE os.path :


print(os.path.basename(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) # Retorna o nome base do caminho path. Este é o segundo elemento do par retornado pela passagem de path para a função split(). 

print(os.path.exists(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) # Retorna True se caminho existe

print(time.localtime((os.path.getatime(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")))) #Retorna a hora do último acesso de path. O valor de retorno é um número de ponto flutuante dando o número de segundos desde a Era Unix (veja o módulo time). 
#time.localtime -> transforma os segundos em struct_time
#time.asctime -> transfomra struct_time em uma string

strut_time = (time.localtime((os.path.getatime(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt"))))
asctime = time.asctime(strut_time)
print(f"asctime = {asctime}")

print(os.path.getmtime(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) #mesma coisa do getatime

print(os.path.getctime(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) #Retorna o ctime do sistema que, em alguns sistemas (como Unix) é a hora da última alteração de metadados, e, em outros (como Windows), é a hora de criação de path.

print(os.path.getsize(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) #Retorna o tamanho, em bytes, de path. Levanta OSError se o arquivo não existe ou está inacessível.

print(os.path.join(r"C:\Users\Asus\Documents\GitHub",r"\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) #Junte-se a um ou mais componentes do caminho de forma inteligente. O valor de retorno é a concatenação de caminho e quaisquer membros de * caminhos com exatamente um separador de diretório após cada parte não vazia, exceto a última, o que significa que o resultado só terminará em um separador se a última parte estiver vazia.

print(os.path.split(r"C:\Users\Asus\Documents\GitHub\manipulacao-dados-python\cap-dois\documentos\dados2.txt")) #Divide o caminho path em um par, (cabeça, rabo) onde rabo é o último componente do nome do caminho e cabeça é tudo o que leva a isso. 




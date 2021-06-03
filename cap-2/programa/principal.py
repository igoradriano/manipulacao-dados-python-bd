import xlrd
from modelos import Variavel

def extrair_variaveis(dicionario):
    # Alteração
    # planilha = xlrd.open_workbook("dados/dicionario_pessoas.xls")
    planilha = xlrd.open_workbook(dicionario)
    primeira_aba = planilha.sheet_by_index(0)  #pegar a primeira aba da planilha
    #print("Nome:", primeira_aba.name)  #.name -> nome da aba
    #print("Num linhas:", primeira_aba.nrows) #.nrows -> número de linhas da planilha
    #print("Num colunas:", primeira_aba.ncols) #.ncols -> número e colunas da planilha

    variaveis = []
    nova_variavel = None
    for idx,linha in enumerate(primeira_aba.get_rows()): #.get_rows -> generator que retorna uma linha
        #print(linha)
        primeira_celula = linha[0]  # Atributos da célula: ctype e value
        if primeira_celula.ctype == 2:  #number -> tipo do valor da primeira celula da linha
            # Nova Variável
            if nova_variavel:
                #Guarda a ultima variável criada
                variaveis.append(nova_variavel)
            #Variáveis do construtor
            posicao_inicial = linha[0].value #este indice se refere s colunas da linha
            tamanho = linha[1].value
            codigo = linha[2].value
            descricao = linha[4].value
            nova_variavel = Variavel(posicao_inicial, tamanho,codigo, descricao)
            #Variáveis da primeira categoria
            #Alteração
            #categoria_tipo = linha[5].value
            #categoria_descricao_tipo = linha[6].value
            categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
            categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
            nova_variavel.add_categoria({'categoria_tipo':categoria_tipo, 'categoria_descricao_tipo': categoria_descricao_tipo})
        else:
            if nova_variavel:
                # Variaveis das demais categorias
                #Alteração
                #categoria_tipo = linha[5].value
                #categoria_descricao_tipo = linha[6].value
                if primeira_celula.ctype == 0:
                    categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
                    categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
                    nova_variavel.add_categoria({'categoria_tipo': categoria_tipo, 'categoria_descricao_tipo': categoria_descricao_tipo})

        #if idx > 50:
           #break

    return variaveis
    #print("Total de variáveis", len(variaveis))
    #for variavel in variaveis:
        #print(variavel)
        #for categ in variavel.categoria:
            #print('\t', categ)
class Variavel:

    def __init__(self, posicao_inicial, tamanho, codigo, descricao):
        self.posicao_inicial = int(posicao_inicial) - 1
        self.tamanho = int(tamanho)
        self.codigo = codigo
        self.descricao = descricao
        # Alteração
        # self.categoria = []
        self.categoria = {}

    def add_categoria(self, categoria):
        # categoria = dict {'categoria_tipo': tipo, 'categoria_descricao_tipo': descricao}
        # Alteração
        # self.categoria.append(categoria)
        self.categoria[categoria.get('categoria_tipo')] = categoria.get("categoria_descricao_tipo")
        # atributo do tipo dicionario da classe Variavel recebe o valor da chave do dicionario categoria passado como  parametro para o método add_categoria
        # Iguala esse valor de chave ao valor da chave 'categoira_descricao_tipo' do dicionario categoria passado como parametro para o método
        # ex: 
        # variavel = Variavel(posicao_inicial, tamanho,codigo, descricao)
        # carro = 'Ferrari'
        # modelo = 'Italia F430'
        # ex: dicionario = {'categoria_tipo': carro, 'categoria_descricao_tipo': modelo}
        # variavel.add_categoria(dicionario)
        # o dicionario categoria da instancia variavel do objeto Variavel recebe -> categoria={'Ferrari':'ItaliaF430'}


    def __str__(self):
        # Alteração
        # return self.codigo + " - " + self.descricao
        return f'{self.codigo} - {self.descricao}'

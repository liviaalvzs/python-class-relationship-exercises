''' Ex3 de Associação Entre Classes
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def excluir_produto(self, indice):
        self.produtos.pop(indice)

    def listar_produtos(self):
        indice = 0
        for produto in self.produtos:
            print(indice, '-', produto.descricao, produto.valor)
            indice += 1

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma


cliente1 = Cliente('Livia Alves')

produto1 = Produto('Livro: O Iluminado', 30)
produto2 = Produto('Fone de Ouvido', 130)
produto3 = Produto('Celular', 900)

carrinho1 = Carrinho(cliente1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto2)
carrinho1.adicionar_produto(produto2)
carrinho1.adicionar_produto(produto3)

carrinho1.listar_produtos()
print('Total da compra:', carrinho1.calcular_total())

indice = int(input('Informe o código do produto para remoção: '))
carrinho1.excluir_produto(indice)
carrinho1.listar_produtos()
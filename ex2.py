'''
|-------------------|           |-------------------|
| Cachorro          |           | Pessoa            |
|-------------------|           |-------------------|
| nome              |0..n   0..1| nome              |
| idade             |-----------| sobrenome         |
| proprietario      |           |                   |
|-------------------|           |-------------------|
|                   |           |                   |
|-------------------|           |-------------------|
'''


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proprietario = []


pessoa1 = Pessoa("Mariazinha", "Sousa")
pessoa2 = Pessoa("Joãozinho", "Silva")

dog = Cachorro("Teddy", 3)
dog.proprietario.append(pessoa1)
dog.proprietario.append(pessoa2)


print("Nome do cachorro: ", dog.nome)
for n in dog.proprietario:
    print(n.nome)
''' PRATICA N° 5
Classe Emprego
Atributos:
cargo
area
salario
bonus: percentual de bonificação a ser acrescentado ao salário do funcionário, de acordo com a quantidade de dependentes. Por exemplo, se o bônus for de 2%, e o funcionário tiver 3 dependentes, ele receberá 6% de acréscimo sobre o salário.
Métodos:
não possui


Classe Pessoa
Atributos:
nome
fone
email
emprego: objeto do tipo Emprego
dependentes: lista de objetos do tipo Pessoa
	Métodos:
calcular_salario: retorna o valor do salário do funcionário, de acordo com o percentual de bonificação e quantidade de dependentes.
'''

class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus

class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []
    
    def calcular_salario(self):
        return (self.emprego.salario + (self.emprego.bonus * len(self.dependentes)))
    
# teste 

emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())                # imprime 1010

'''
Classe Paciente
Atributos:
nome
cpf
idade
Métodos:
não possui

Classe Medico
Atributos:
nome
crm
especializacao
Métodos:
não possui

Classe Exame
Atributos:
medico: objeto da classe Medico
paciente: objeto da classe Paciente
descricao
resultado
Métodos:
imprimir_exame(): exibe um relatório com os dados do exame (inclusive os dados do médico e do paciente)

'''

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame (self):
        print('----- EXAME -----')
        print(f'Paciente: {self.paciente.nome}, {self.paciente.idade} anos')
        print(f'Exame realizado por: {self.medico.nome}, {self.medico.especializacao} | CRM - {self.medico.crm}')
        print(f'DESCRICAO DO EXAME: {self.descricao}')
        print(f'RESULTADO DO EXAME: {self.resultado}')
    
# teste

paciente = Paciente('Livia Alves', '033444555-22', 17)
medico = Medico('Ana Maria', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)




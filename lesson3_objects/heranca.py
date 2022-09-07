### herança ###

### imaginemos um funcionario comum ###
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'Nome':self.nome, 'Salario':self.salario}

    pass

### agora vamos criar um administrador          ###
### que herda as caracteristicas do funcionario ###
class Administrador(Funcionario):
    def __init__(self, nome, salario):
        self.email = ''
        super().__init__(nome, salario)

    def set_email(self, email):
        self.email = email

    def dados(self):
        return {'Nome': self.nome, 'Salario': self.salario, 'Email': self.email}

    pass

# cria um funcionario
Jose = Funcionario('José', 3000.00)
print(Jose.dados())
#imprime {'Nome': 'José', 'Salario': 3000.0}

# cria um admninistrador
Carlos = Administrador('Carlos', 10000)
Carlos.set_email('cgmodel@gmail.com')
print(Carlos.dados())
# imprime {'Nome': 'Carlos', 'Salario': 10000, 'Email': 'cgmodel@gmail.com'}
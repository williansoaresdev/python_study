### metodos de classes e metodos estaticos ###

### imaginemos um funcionario   ###
### porém agora a classe possui ###
### um metodo estatico especial ###
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'Nome':self.nome, 'Salario':self.salario}

    @staticmethod
    def nome_do_cargo():
        return 'Funcionário'

    pass

# veja que vamos usar o método sem nem mesmo
# precisar criar uma instância
# (para isso o método não pode usar atributos do objeto)

print (Funcionario.nome_do_cargo())
#imprime Funcionário
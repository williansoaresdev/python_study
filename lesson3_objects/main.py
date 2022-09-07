### classes e objetos ###

# modelo padrao de uma classe

class jogador:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 38

    def dobro_idade(self):
        return self.idade * 2
    
    pass

# como instanciar

jogador1 = jogador('José')

jogador2 = jogador('Maria')

print('Jogador {} tem {} x 2 = {}'.format(jogador1.nome, jogador1.idade, jogador1.dobro_idade()))
# imprime Jogador José tem 38 x 2 = 76


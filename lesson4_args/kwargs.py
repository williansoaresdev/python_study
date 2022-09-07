### kwargs são argumentos com palavras chave ###

def gera_personagem(nome, **kwargs):
    print("Personagem {} =>".format(nome))
    print(kwargs)

gera_personagem('Will', Sobrenome='Soares',Idade=38)

# imprime
# Personagem Will =>
# {'Sobrenome': 'Soares', 'Idade': 38}
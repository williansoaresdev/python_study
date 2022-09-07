### argumentos e palavras chave ###

## argumentos permite que vc crie uma função
## onde você não sabe o número de parâmetros esperado

## exemplo:
## uma rotina de soma que recebe qualquer
## quantidade de numeros para somar
def soma_numeros(*args):
    return sum(args)

# testando:
print(soma_numeros(7,2,9))
# imprime 18
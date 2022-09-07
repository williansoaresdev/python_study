# lista com tratamento da varivavel

# neste exemplo, para cada x no range de 0 a 4
# irá multiplicar por 2 e incluir na lista resultante
minhaLista = [x * 2 for x in range(5)]

print(minhaLista)
# apresenta [0, 2, 4, 6, 8]

# partiu imprimir item a item da lista?
for x in minhaLista:
    print(x);

# vamos criar uma lista bagunçada de pessoas
pessoas = [' will ', 'ROBERTA', 'arthur']

# agora vamos criar uma lista normalizada
pessoasOK = [pessoa.strip().capitalize() for pessoa in pessoas]

print(pessoasOK)
# apresenta ['Will', 'Roberta', 'Arthur']
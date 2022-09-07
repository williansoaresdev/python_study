# usando dicionarios

# composto por chaves e valores
# similar a um JSON

dic_will = {'Nome':'Willian', 'Idade': 38}

print(dic_will)
# imprime {'Nome': 'Willian', 'Idade': 38}

# acessando um valor individual

print(dic_will['Nome'])
# imprime Willian

# lista de dicionarios
list_people = [{'Nome':'Will'},{'Nome':'Roberta'}]

print(list_people)
# imprime [{'Nome': 'Will'}, {'Nome': 'Roberta'}]

print(list_people[0])
# imprime {'Nome': 'Will'}

print(list_people[1]['Nome'])
# imprime Roberta
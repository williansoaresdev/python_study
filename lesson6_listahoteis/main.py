### retornando uma lista de hoteis ###

# Importacoes basicas necessarias
from flask import Flask
from flask_restful import Resource, Api

# Instanciando a Api 
app = Flask(__name__)
api = Api(app)

# lista na memoria de hoteis
hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.5,
        'cidade': 'Garujá'
    },
    {
        'hotel_id': 'boreal',
        'nome': 'Boreal Hotel',
        'estrelas': 4.7,
        'diaria': 399.5,
        'cidade': 'Gramado'
    },
    {
        'hotel_id': 'dubai',
        'nome': 'Dubai Star Hotel',
        'estrelas': 4.5,
        'diaria': 400.00,
        'cidade': 'Rio de Janeiro'
    }
]

# criando a classe a partir do recurso da Api
class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}

# adiciono meu novo recurso na api
api.add_resource(Hoteis, '/hoteis')

# executa imediatamente se estiver rodando este app como principal
if __name__ == '__main__':
    # modo debug somente durante desenvolvimento
    app.run(debug=True)
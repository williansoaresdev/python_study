from flask_restful import Resource

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

# criando as classes a partir do recurso da Api
class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
            return {'message':'Hotel not found.'}, 404
        pass

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
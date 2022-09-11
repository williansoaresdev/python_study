from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    # configuramos nosso parser
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        busca_hotel = self.find_hotel(hotel_id)
        if busca_hotel == None:
            return {'message':'Hotel not found.'}, 404
        else:
            return busca_hotel

    def post(self, hotel_id):

        # processamos nosso parser
        dados = self.argumentos.parse_args()

        # montamos o objeto a ser incluido na lista de hoteis
        novo_hotel = HotelModel(hotel_id, **dados).json()

        # gravamos o hotel em nossa lista
        hoteis.append(novo_hotel)

        # retornamos o hotel gerado no JSON do cliente
        return novo_hotel, 200

    def put(self, hotel_id):
        # processamos nosso parser
        dados = self.argumentos.parse_args()

        # montamos o objeto a ser incluido na lista de hoteis
        novo_hotel = HotelModel(hotel_id, **dados).json()

        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        # var global de hoteis
        global hoteis
        # vamos usar list comprehension para criar uma lista removendo o hotel desejado
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        # traga cada hotel de hoteis SE hotel_id for diferente do hotel_id enviado...

        return {'message':'Hotel deleted.'}
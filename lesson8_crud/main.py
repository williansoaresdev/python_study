### retornando uma lista de hoteis ###

# Importacoes basicas necessarias
from flask import Flask
from flask_restful import Api
# importa o recurso da nossa propria pasta
from resources.hotel import Hoteis, Hotel

# Instanciando a Api 
app = Flask(__name__)
api = Api(app)

# adiciono meu novo recurso na api
api.add_resource(Hoteis, '/hoteis')
# recursos para o crud de Hotel
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

# executa imediatamente se estiver rodando este app como principal
if __name__ == '__main__':
    # modo debug somente durante desenvolvimento
    app.run(debug=True)
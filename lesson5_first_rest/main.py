### criando nossa primeira aplicação rest ###

# Importacoes basicas necessarias
from flask import Flask
from flask_restful import Resource, Api

# Instanciando a Api 
app = Flask(__name__)
api = Api(app)

# criando a classe a partir do recurso da Api
class Hoteis(Resource):
    def get(self):
        return {'hoteis':'meus hoteis(a desenvolver)'}

# adiciono meu novo recurso na api
api.add_resource(Hoteis, '/hoteis')

# executa imediatamente se estiver rodando este app como principal
if __name__ == '__main__':
    # modo debug somente durante desenvolvimento
    app.run(debug=True)
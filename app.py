from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from models import db
from resources import (ClienteResource, ClienteListResource,
                       StatusChamadoListResource, StatusChamadoResource,
                       UsuarioResource, UsuarioListResource, TecnicoResource,TecnicoListResource
                       , ChamadoListResource, ChamadoResource)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)  # Adicionando a configuração de migração
api = Api(app)

api.add_resource(ClienteListResource, '/clientes')
api.add_resource(ClienteResource, '/clientes/<int:id>')
api.add_resource(StatusChamadoListResource, '/status_chamado')
api.add_resource(StatusChamadoResource, '/status_chamado/<int:id>')
# Rotas para Usuario
api.add_resource(UsuarioResource, '/usuarios/<int:id>')
api.add_resource(UsuarioListResource, '/usuarios')
api.add_resource(TecnicoListResource, '/tecnicos')
api.add_resource(TecnicoResource, '/tecnicos/<int:id>')
api.add_resource(ChamadoListResource, '/chamados')
api.add_resource(ChamadoResource, '/chamados/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)

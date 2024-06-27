from flask_restful import Resource
from flask import request
from models import db, Cliente, StatusChamado, Usuario, Tecnico, Chamado
from schemas import ClienteSchema, UsuarioSchema, TecnicoSchema, ChamadoSchema

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)


class ClienteResource(Resource):
    def get(self, id):
        cliente = Cliente.query.get_or_404(id)
        return cliente_schema.dump(cliente)

    def put(self, id):
        cliente = Cliente.query.get_or_404(id)
        data = request.get_json()
        cliente.nome = data.get('nome', cliente.nome)
        cliente.email = data.get('email', cliente.email)
        cliente.telefone = data.get('telefone', cliente.telefone)
        cliente.cpf = data.get('cpf', cliente.cpf)
        cliente.rg = data.get('rg', cliente.rg)
        db.session.commit()
        return cliente_schema.dump(cliente)

    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204


class ClienteListResource(Resource):
    def get(self):
        clientes = Cliente.query.all()
        return clientes_schema.dump(clientes)

    def post(self):
        data = request.get_json()
        cliente = Cliente(
            nome=data['nome'],
            email=data['email'],
            telefone=data['telefone'],
            cpf=data['cpf'],
            rg=data['rg']
        )
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201

class StatusChamadoResource(Resource):
    def get(self, id):
        status = StatusChamado.query.get_or_404(id)
        return {'id': status.id, 'descricao': status.descricao}

    def put(self, id):
        status = StatusChamado.query.get_or_404(id)
        data = request.get_json()
        status.descricao = data.get('descricao', status.descricao)
        db.session.commit()
        return {'id': status.id, 'descricao': status.descricao}

    def delete(self, id):
        status = StatusChamado.query.get_or_404(id)
        db.session.delete(status)
        db.session.commit()
        return '', 204

class StatusChamadoListResource(Resource):
    def get(self):
        status_list = StatusChamado.query.all()
        return [{'id': status.id, 'descricao': status.descricao} for status in status_list]

    def post(self):
        data = request.get_json()
        descricao = data.get('descricao')
        novo_status = StatusChamado(descricao=descricao)
        db.session.add(novo_status)
        db.session.commit()
        return {'id': novo_status.id, 'descricao': novo_status.descricao}, 201


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class UsuarioResource(Resource):
    def get(self, id):
        usuario = Usuario.query.get_or_404(id)
        return usuario_schema.dump(usuario)

    def put(self, id):
        usuario = Usuario.query.get_or_404(id)
        data = request.get_json()
        usuario.login = data.get('login', usuario.login)
        usuario.senha = data.get('senha', usuario.senha)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204


class UsuarioListResource(Resource):
    def post(self):
        data = request.get_json()

        # Validar se todos os campos necessários foram fornecidos
        if not data.get('login') or not data.get('senha'):
            return {'message': 'Os campos login e senha são obrigatórios.'}, 400

        # Verificar se já existe um usuário com o mesmo login
        existing_usuario = Usuario.query.filter_by(login=data['login']).first()
        if existing_usuario:
            return {'message': 'Já existe um usuário com este login.'}, 400

        # Criar um novo usuário com os dados fornecidos
        novo_usuario = Usuario(
            login=data['login'],
            senha=data['senha']
        )

        # Adicionar ao banco de dados
        db.session.add(novo_usuario)
        db.session.commit()

        # Retornar os dados do novo usuário criado
        return usuario_schema.dump(novo_usuario), 201

    def get(self):
        usuarios = Usuario.query.all()
        return [{'id': usuario.id,'login': usuario.login, 'senha': usuario.senha} for usuario in usuarios], 200

tecnico_schema = TecnicoSchema()
tecnicos_schema = TecnicoSchema(many=True)

class TecnicoResource(Resource):
    def get(self, id):
        tecnico = Tecnico.query.get_or_404(id)
        return tecnico_schema.dump(tecnico)

    def put(self, id):
        tecnico = Tecnico.query.get_or_404(id)
        data = request.get_json()
        tecnico.nome = data.get('nome', tecnico.nome)
        tecnico.cpf = data.get('cpf', tecnico.cpf)
        tecnico.rg = data.get('rg', tecnico.rg)
        tecnico.ativo = data.get('ativo', tecnico.ativo)
        tecnico.id_usuario = data.get('id_usuario', tecnico.id_usuario)
        db.session.commit()
        return tecnico_schema.dump(tecnico)

    def delete(self, id):
        tecnico = Tecnico.query.get_or_404(id)
        db.session.delete(tecnico)
        db.session.commit()
        return '', 204

class TecnicoListResource(Resource):
    def get(self):
        tecnicos = Tecnico.query.all()
        return tecnicos_schema.dump(tecnicos)

    def post(self):
        data = request.get_json()
        tecnico = Tecnico(
            nome=data['nome'],
            cpf=data.get('cpf'),
            rg=data.get('rg'),
            ativo=data.get('ativo', True),
            id_usuario=data.get('id_usuario')
        )
        db.session.add(tecnico)
        db.session.commit()
        return tecnico_schema.dump(tecnico), 201


chamado_schema = ChamadoSchema()
chamados_schema = ChamadoSchema(many=True)

class ChamadoResource(Resource):
    def get(self, id):
        chamado = Chamado.query.get_or_404(id)
        return chamado_schema.dump(chamado)

    def put(self, id):
        chamado = Chamado.query.get_or_404(id)
        data = request.get_json()
        chamado.id_cliente = data.get('id_cliente', chamado.id_cliente)
        chamado.id_tecnico = data.get('id_tecnico', chamado.id_tecnico)
        chamado.descricao = data.get('descricao', chamado.descricao)
        chamado.data_fechamento = data.get('data_fechamento', chamado.data_fechamento)
        chamado.id_status = data.get('id_status', chamado.id_status)
        db.session.commit()
        return chamado_schema.dump(chamado)

    def delete(self, id):
        chamado = Chamado.query.get_or_404(id)
        db.session.delete(chamado)
        db.session.commit()
        return '', 204

class ChamadoListResource(Resource):
    def get(self):
        chamados = Chamado.query.all()
        return chamados_schema.dump(chamados)

    def post(self):
        data = request.get_json()
        chamado = Chamado(
            id_cliente=data['id_cliente'],
            id_tecnico=data['id_tecnico'],
            descricao=data['descricao'],
            id_status=data['id_status']
        )
        db.session.add(chamado)
        db.session.commit()
        return chamado_schema.dump(chamado), 201
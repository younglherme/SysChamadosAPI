from marshmallow import Schema, fields

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    telefone = fields.Str(required=True)
    cpf = fields.Str(required=True)
    rg = fields.Str(required=True)


class StatusChamadoSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True)

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    login = fields.Str(required=True)
    senha = fields.Str(required=True)

from marshmallow import Schema, fields

class TecnicoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    cpf = fields.Str()
    rg = fields.Str()
    ativo = fields.Bool()
    id_usuario = fields.Int()


class ChamadoSchema(Schema):
    id = fields.Int(dump_only=True)
    id_cliente = fields.Int(required=True)
    id_tecnico = fields.Int(required=True)
    descricao = fields.Str(required=True)
    data_abertura = fields.DateTime(dump_only=True)
    data_fechamento = fields.DateTime()
    id_status = fields.Int(required=True)

    cliente = fields.Nested(ClienteSchema, dump_only=True)
    tecnico = fields.Nested(TecnicoSchema, dump_only=True)
    status = fields.Nested(StatusChamadoSchema, dump_only=True)

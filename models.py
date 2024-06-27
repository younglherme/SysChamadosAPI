from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    cpf = db.Column(db.String(100))
    rg = db.Column(db.String(100))

    def __init__(self, nome, email, telefone, cpf, rg):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.rg = rg

class StatusChamado(db.Model):
    __tablename__ = 'status_chamado'
    id = db.Column(db.BigInteger, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

class Tecnico(db.Model):
    __tablename__ = 'tecnicos'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100))
    rg = db.Column(db.String(100))
    ativo = db.Column(db.Boolean, default=True)
    id_usuario = db.Column(db.BigInteger, db.ForeignKey('usuarios.id'))

    def __repr__(self):
        return f'<Tecnico {self.id}, {self.nome}>'

class Chamado(db.Model):
    __tablename__ = 'chamados'
    id = db.Column(db.BigInteger, primary_key=True)
    id_cliente = db.Column(db.BigInteger, db.ForeignKey('clientes.id'), nullable=False)
    id_tecnico = db.Column(db.BigInteger, db.ForeignKey('tecnicos.id'), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_abertura = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_fechamento = db.Column(db.DateTime)
    id_status = db.Column(db.BigInteger, db.ForeignKey('status_chamado.id'), nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('chamados', lazy=True))
    tecnico = db.relationship('Tecnico', backref=db.backref('chamados', lazy=True))
    status = db.relationship('StatusChamado', backref=db.backref('chamados', lazy=True))

from . import db

class Imovel(db.Model):
    __tablename__ = 'Imoveis'

    id = db.Column(db.Integer, db.Identity(), primary_key = True)
    logradouro = db.Column(db.String())
    cep = db.Column(db.Integer())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())

    # def __init__(self, id, logradouro, cep, bairro, cidade):
    #     self.id = id
    #     self.logradouro = logradouro
    #     self.cep = cep
    #     self.bairro = bairro
    #     self.cidade = cidade

    def __repr__(self):
        return f"<Imovel {self.logradouro}, {self.cidade}.>"

class Individuo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    data_de_nascimento = db. Column(db.String())

    def __init__(self, id, nome, data_de_nascimento):
        self.id = id
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    def __repr__(self):
        return f"<Individuo {self.id}: {self.nome}, nascida(o) em {self.data_de_nascimento}.>"

    
class Inquilino(db.Model):
    __tablename__ = 'Inquilinos'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    data_de_nascimento = db. Column(db.String())

    def __init__(self, id, nome, data_de_nascimento):
        self.id = id
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    def __repr__(self):
        return f"<Proprietario {self.id}: {self.nome}, nascida(o) em {self.data_de_nascimento}>"

    
class Proprietario(db.Model):
    __tablename__ = 'Proprietarios'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    data_de_nascimento = db. Column(db.String())


    def __init__(self, id, nome, data_de_nascimento):
        self.id = id
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    def __repr__(self):
        return f"<Proprietario {self.id}: {self.nome}, nascida(o) em {self.data_de_nascimento}>"


class Aluguel(db.Model):
    __tablename__ = 'Alugueis'

    id = db.Column(db.Integer, primary_key = True)
    imovel = db.Column(db.Integer, db.ForeignKey('Imoveis.id'))
    proprietario = db.Column(db.Integer, db.ForeignKey('Proprietarios.id'))

    def init(self, id, imovel, proprietario):
        self.id = id,
        self.imovel = imovel,
        self.proprietario = proprietario

    def __repr__(self):
        return f"<Aluguel id: {self.id}, id imovel: {self.imovel}, id proprietario: {self.proprietario}."


class Contrato(db.Model):
    __tablename__ = 'Contratos'

    id = db.Column(db.Integer, primary_key = True)
    aluguel = db.Column(db.Integer, db.ForeignKey('Alugueis.id'))
    inquilino = db.Column(db.Integer, db.ForeignKey('Inquilinos.id'))

    def __init__(self, id, aluguel, inquilino):
        self.id = id,
        self.aluguel = aluguel,
        self.inquilino = inquilino

    def __repr__(self):
        return "<Contrato de Inquilino {self.inquilino} no Aluguel {self.aluguel}.>"


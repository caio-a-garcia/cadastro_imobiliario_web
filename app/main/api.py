from flask import request
from . import main
from .. import db
from ..models import Imovel, Inquilino, Proprietario, Aluguel, Contrato

@main.route('/imoveis', methods=['POST', 'GET'])
def handle_imoveis():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_imovel = Imovel(id = data['id'],
                                logradouro = data['logradouro'],
                                cep = data['cep'],
                                bairro = data['bairro'],
                                cidade = data['cidade'],
                                )
            db.session.add(new_imovel)
            db.session.commit()
            return {"message": f"Imovel {new_imovel.logradouro}, {new_imovel.cidade} foi criado com sucesso."}
        else:
            return {"error": "O payload da request nao esta em formato JSON."}

    elif request.method == 'GET':
        imoveis = Imovel.query.all()
        results = [
            {
                "id": imovel.id,
                "logradouro": imovel.logradouro,
                "cep": imovel.cep,
                "bairro": imovel.bairro,
                "cidade": imovel.cidade
            } for imovel in imoveis]

        return {"total": len(results), "imoveis": results}


@main.route('/imoveis/<imovel_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_imovel(imovel_id):
    imovel = Imovel.query.get_or_404(imovel_id)

    if request.method == 'GET':
        response = {
            "id": imovel.id,
            "logradouro": imovel.logradouro,
            "cep": imovel.cep,
            "bairro": imovel.bairro,
            "cidade": imovel.cidade
        }
        return {"message": "success", "imovel": response}

    elif request.method == 'PUT':
        data = request.get_json()
        imovel.id = data['id']
        imovel.logradouro = data['logradouro']
        imovel.cep = data['cep']
        imovel.bairro = data['bairro']
        imovel.cidade = data['cidade']
        db.session.add(imovel)
        db.session.commit()
        return {"message": f"Imovel {imovel.logradouro}, {imovel.cidade} modificado com sucesso."}

    elif request.method == 'DELETE':
        db.session.delete(imovel)
        db.session.commit()
        return {"message": f"Imovel {imovel.logradouro}, {imovel.cidade} apagado com sucesso."}

# Proprietarios
@main.route('/proprietarios', methods=['POST', 'GET'])
def handle_proprietarios():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_proprietario = Proprietario(id = data['id'],
                                nome = data['nome'],
                                data_de_nascimento = data['data_de_nascimento'],
                                            )
            db.session.add(new_proprietario)
            db.session.commit()
            return {"message": f"Proprietario {new_proprietario.id}: {new_proprietario.nome} foi registrado com sucesso."}
        else:
            return {"error": "O payload da request nao esta em formato JSON."}

    elif request.method == 'GET':
        proprietarios = Proprietario.query.all()
        results = [
            {
                "id": proprietario.id,
                "nome": proprietario.nome,
                "data de nascimento": proprietario.data_de_nascimento,
            } for proprietario in proprietarios]

        return {"total": len(results), "proprietarios": results}


@main.route('/proprietarios/<proprietario_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_proprietario(proprietario_id):
    proprietario = Proprietario.query.get_or_404(proprietario_id)

    if request.method == 'GET':
        response = {
            "id": proprietario.id,
            "nome": proprietario.nome,
            "data de nascimento": proprietario.data_de_nascimento,
        }
        return {"message": "success", "proprietario": response}

    elif request.method == 'PUT':
        data = request.get_json()

        proprietario.id = data['id']
        proprietario.nome = data['nome']
        proprietario.data_de_nascimento = data['data de nascimento']

        db.session.add(proprietario)
        db.session.commit()
        return {"message": f"Proprietario {proprietario.id}: {proprietario.nome} modificado com sucesso."}

    elif request.method == 'DELETE':
        db.session.delete(proprietario)
        db.session.commit()
        return {"message": f"Proprietario {proprietario.id}: {proprietario.nome} apagado com sucesso."}


# Inquilinos
@main.route('/inquilinos', methods=['POST', 'GET'])
def handle_inquilinos():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_inquilino = Inquilino(id = data['id'],
                                nome = data['nome'],
                                data_de_nascimento = data['data_de_nascimento'],
                                )
            db.session.add(new_inquilino)
            db.session.commit()
            return {"message": f"Inquilino {new_inquilino.id}: {new_inquilino.nome} foi registrado com sucesso."}
        else:
            return {"error": "O payload da request nao esta em formato JSON."}

    elif request.method == 'GET':
        inquilinos = Inquilino.query.all()
        results = [
            {
                "id": inquilino.id,
                "nome": inquilino.nome,
                "data de nascimento": inquilino.data_de_nascimento,
            } for inquilino in inquilinos]

        return {"total": len(results), "inquilinos": results}


@main.route('/inquilinos/<inquilino_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_inquilino(inquilino_id):
    inquilino = Inquilino.query.get_or_404(inquilino_id)

    if request.method == 'GET':
        response = {
            "id": inquilino.id,
            "nome": inquilino.nome,
            "data de nascimento": inquilino.data_de_nascimento,
        }
        return {"message": "success", "inquilino": response}

    elif request.method == 'PUT':
        data = request.get_json()

        inquilino.id = data['id']
        inquilino.nome = data['nome']
        inquilino.data_de_nascimento = data['data de nascimento']

        db.session.add(inquilino)
        db.session.commit()
        return {"message": f"Inquilino {inquilino.id}: {inquilino.nome} modificado com sucesso."}

    elif request.method == 'DELETE':
        db.session.delete(inquilino)
        db.session.commit()
        return {"message": f"Inquilino {inquilino.id}: {inquilino.nome} apagado com sucesso."}


# Alugueis
@main.route('/alugueis', methods=['POST', 'GET'])
def handle_alugueis():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_aluguel = Aluguel(id = data['id'],
                                imovel = data['imovel'],
                                proprietario = data['proprietario'],
                                )
            db.session.add(new_aluguel)
            db.session.commit()
            return {"message": f"Aluguel {new_aluguel.id} foi registrado com sucesso."}
        else:
            return {"error": "O payload da request nao esta em formato JSON."}

    elif request.method == 'GET':
        alugueis = Aluguel.query.all()
        results = [
            {
                "id": aluguel.id,
                "imovel": aluguel.imovel,
                "proprietario": aluguel.proprietario,
            } for aluguel in alugueis]

        return {"total": len(results), "alugueis": results}


@main.route('/alugueis/<aluguel_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_aluguel(aluguel_id):
    aluguel = Aluguel.query.get_or_404(aluguel_id)

    if request.method == 'GET':
        response = {
            "id": aluguel.id,
            "imovel": aluguel.imovel,
            "proprietario": aluguel.proprietario,
        }
        return {"message": "success", "aluguel": response}

    elif request.method == 'PUT':
        data = request.get_json()

        aluguel.id = data['id']
        aluguel.imovel = data['imovel']
        aluguel.proprietario = data['proprietario']

        db.session.add(aluguel)
        db.session.commit()
        return {"message": f"Aluguel {aluguel.id} modificado com sucesso."}

    elif request.method == 'DELETE':
        db.session.delete(aluguel)
        db.session.commit()
        return {"message": f"Aluguel {aluguel.id} apagado com sucesso."}

# Contratos
@main.route('/contratos', methods=['POST', 'GET'])
def handle_contratos():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_contrato = Contrato(id = data['id'],
                                aluguel = data['aluguel'],
                                inquilino = data['inquilino'],
                                )
            db.session.add(new_contrato)
            db.session.commit()
            return {"message": f"Contrato {new_contrato.id} foi registrado com sucesso."}
        else:
            return {"error": "O payload da request nao esta em formato JSON."}

    elif request.method == 'GET':
        contratos = Contrato.query.all()
        results = [
            {
                "id": contrato.id,
                "aluguel": contrato.aluguel,
                "inquilino": contrato.inquilino,
            } for contrato in contratos]

        return {"total": len(results), "contratos": results}


@main.route('/contratos/<contrato_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_contrato(contrato_id):
    contrato = Contrato.query.get_or_404(contrato_id)

    if request.method == 'GET':
        response = {
            "id": contrato.id,
            "aluguel": contrato.aluguel,
            "inquilino": contrato.inquilino,
        }
        return {"message": "success", "contrato": response}

    elif request.method == 'PUT':
        data = request.get_json()

        contrato.id = data['id']
        contrato.aluguel = data['aluguel']
        contrato.inquilino = data['inquilino']

        db.session.add(contrato)
        db.session.commit()
        return {"message": f"Contrato {contrato.id} modificado com sucesso."}

    elif request.method == 'DELETE':
        db.session.delete(contrato)
        db.session.commit()
        return {"message": f"Contrato {contrato.id} apagado com sucesso."}


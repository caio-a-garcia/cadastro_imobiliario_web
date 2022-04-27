from flask import render_template, abort, url_for
from . import main, api
from .. import db
from .forms import FormImoveis, FormProprietarios, FormInquilinos, FormAlugueis, FormContratos

#########
# Front #
######### -request, ..models
@main.route('/', methods=['GET'])
def handle_index():
    return render_template('index.html')


@main.route('/listar/<lista>', methods=['GET'])
def handle_listar_itens(lista):
    opcoes = {
        'imoveis': api.handle_imoveis(),
        'proprietarios':api.handle_proprietarios(),
        'inquilinos': api.handle_inquilinos(),
        'alugueis': api.handle_alugueis(),
        'contratos': api.handle_contratos()
    }
    if lista in opcoes:
        itens = opcoes[lista]
        return render_template('listar_itens.html', lista = lista, itens = itens)
    else:
        abort(404)

@main.route('/listar/<lista>/<id>', methods=['GET'])
def handle_mostrar_item(lista, id):
    opcoes = {
        'imoveis': handle_imovel,
        'proprietarios': handle_proprietario,
        'inquilinos': handle_inquilino,
        'alugueis': handle_aluguel,
        'contratos': handle_contrato
    }
    if lista in opcoes:
        item = opcoes[lista](id)
        return render_template('mostrar_item.html', lista = lista, item = item)
    else:
        abort(404)

@main.route('/post/<lista>', methods=['GET'])
def handle_post_item(lista):
    templates = {
                 'imoveis': 'post_imoveis.html',
                 'proprietarios': 'post_proprietarios.html',
                 'inquilinos': 'post_inquilinos.html',
                 'alugueis': 'post_alugueis.html',
                 'contratos': 'post_contratos.html'
    }
    forms = {
                'imoveis': FormImoveis,
                'proprietarios': FormProprietarios,
                'inquilinos': FormInquilinos,
                'alugueis': FormAlugueis,
                'contratos': FormContratos
    }
    form = forms[lista]()
    return render_template(templates[lista], lista = lista, form = form)


#######            
# API #
####### -abort, render_template, forms

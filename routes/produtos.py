from flask import render_template, request, Blueprint, flash, redirect, url_for
from models.produtos import Produtos, mysql_db
from peewee import IntegrityError

rota_produtos = Blueprint('produtos', __name__)

mysql_db.connect()

@rota_produtos.route('/')
def listarProdutos():
    produtos = Produtos.select()
    return render_template('listar_produtos.html', produtos=produtos)

@rota_produtos.route('/adicionar')
def form_adicionar():
    return render_template('adicionar.html')

@rota_produtos.route('/', methods=["POST"])
def adicionar():
    id = int(request.form['id'])
    nome = request.form['nome'].strip()
    descricao = request.form['descricao'].strip()
    preco = float(request.form['preco'])
    quantidade = int(request.form['quantidade'])
        
    produto_existente = Produtos.select().where(Produtos.id == id).first()
    
    if produto_existente:
        return redirect(url_for('produtos.form_adicionar')), 302
    else:
        novo_produto = Produtos.create(id=id, nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        return render_template('produto.html', produto=novo_produto), 200
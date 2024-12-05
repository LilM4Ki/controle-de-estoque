import flask
from flask import (Blueprint, Flask, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import login_user, logout_user

from models.registro import Usuarios, mysql_db

auth_route = Blueprint('auth', __name__)

@auth_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usernameForm'].lower()
        senha = request.form['senhaForm']
        
        user = Usuarios.get_or_none(Usuarios.username == username)
        if user and user.senha == senha:
            login_user(user)
            response = jsonify({"message": "Login bem-sucedido"})
            response.headers['HX-Redirect'] = url_for('home.home')
            return response
        else:
            flash('Usuário ou senha incorretos')
            response = jsonify({"message": "Login mal-sucedido"})
            response.headers['HX-Redirect'] = url_for('auth.login')
            return response, 403
    return render_template('login.html')

@auth_route.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['usernameForm'].lower()
        senha = request.form['senhaForm']
        
        if not Usuarios.get_or_none(Usuarios.username == username):
            user = Usuarios(username=username, senha=senha)
            user.save()
            response = jsonify({"message": "Login bem-sucedido"})
            response.headers['HX-Redirect'] = url_for('auth.login')
            return response
        else:
            flash('Usuário já existente')
            response = jsonify({"message": "Login mal-sucedido"})
            response.headers['HX-Redirect'] = url_for('auth.register')
            return response, 403
    return render_template('register.html')

@auth_route.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

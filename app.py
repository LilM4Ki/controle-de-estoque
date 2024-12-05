import os

from dotenv import load_dotenv
from flask import Blueprint, Flask, render_template
from flask_login import LoginManager

from models.registro import Usuarios
from routes.auth import auth_route
from routes.home import home_route
from routes.produtos import rota_produtos

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRETKEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def user_loader(id):
    return Usuarios.get_or_none(Usuarios.id == id)

app.register_blueprint(home_route)
app.register_blueprint(rota_produtos, url_prefix='/produtos')
app.register_blueprint(auth_route, url_prefix="/auth")


app.run(debug=True)
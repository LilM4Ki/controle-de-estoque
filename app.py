from flask import Flask

from routes.home import home_route
from routes.produtos import rota_produtos

app = Flask(__name__)
app.secret_key = 'secretkey'
app.register_blueprint(home_route)
app.register_blueprint(rota_produtos, url_prefix='/produtos')


app.run(debug=True)
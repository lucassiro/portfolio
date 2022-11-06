# https://www.youtube.com/watch?v=XPPYPb3ByiM

from flask import Flask
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)

db.init_app(app)
conexao = "sqlite:///meubanco.sqlite"

app.config["SECRET_KEY"] = "minha-chave"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False
app.register_blueprint(bp_usuarios, url_prefix="/usuarios")

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Hello World"

app.run(host="0.0.0.0", port=81, debug=True)
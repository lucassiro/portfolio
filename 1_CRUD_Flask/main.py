# https://www.youtube.com/watch?v=XPPYPb3ByiM

from flask import Flask
from database import db
from flask_migrate import Migrate
from users import bp_users

app = Flask(__name__)

db.init_app(app)
conection = "sqlite:///database.sqlite"

app.config["SECRET_KEY"] = "my-key"
app.config["SQLALCHEMY_DATABASE_URI"] = conection
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False
app.register_blueprint(bp_users, url_prefix="/users")

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Hello World"

app.run(host="0.0.0.0", port=81, debug=True)

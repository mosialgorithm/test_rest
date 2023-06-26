import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

bsdir = os.path.abspath(os.path.dirname(__file__))
print(bsdir)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(bsdir,'data.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = "mostafa_ghorbani"


api = Api(app)

db = SQLAlchemy(app)

ma = Marshmallow(app)

# jwt = JWTManager(app)



# ==================== URL Routs =====================
from item import item
from store import store


app.register_blueprint(item)
app.register_blueprint(store)
# ====================================================



@app.before_request
def create_tables():
    db.create_all()



if __name__ == "__main__":
    app.run(debug=True)





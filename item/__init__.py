from flask import Blueprint


item = Blueprint('item', __name__, url_prefix='/item/')


from . import resources

from .models import ItemModel
from marshmallow_sqlalchemy import ModelSchema
from app import db



class ItemSchema(ModelSchema):
    class Meta:
        model = ItemModel
        
        load_only = ("store", )
        dump_only = ("id",  )
        
        include_fk = True
        include_relationships = True
        
        load_instance = True
        sqla_session = db.session
        
        
        

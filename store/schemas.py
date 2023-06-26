from .models import StoreModel
from marshmallow_sqlalchemy import ModelSchema, fields
from app import db
from item.schemas import ItemSchema



class StoreSchema(ModelSchema):
    items = fields.Nested(ItemSchema, many=True)
    
    class Meta:
        model = StoreModel
        
        load_only = ()
        dump_only = ("id","name", "items",)
        
        include_fk = True
        include_relationships = True
        
        load_instance = True
        sqla_session = db.session
        
        
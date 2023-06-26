from flask_restful import Resource
from flask import request
from .models import ItemModel
from .schemas import ItemSchema
from . import item
from app import db


item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)


# =======================================
# new item 
# =======================================
@item.route('/new', methods=['POST'])
def item_new():
    item_json = request.get_json()
    # --------------- prevent duplicate item -----------------------
    name = item_json["name"]
    if ItemModel.query.filter_by(name=name).first():
        return {"message" : "this name is already exists"}
    # --------------------------------------------------------------
    item = item_schema.load(item_json)

    try:
        db.session.add(item)
        db.session.commit()
    except Exception as ex:
        return {"message" : f"{ex}"}
        
    return item_schema.dump(item), 201


# =======================================
# get all items
# =======================================
@item.route('/list', methods=['GET'])
def item_list():
    all_items = item_list_schema.dump(ItemModel.query.all())
    return {"items" : all_items}


# =======================================
# get item information
# =======================================
@item.route('/<string:item_name>', methods=['GET'])
def get_item(item_name):
    item = ItemModel.query.filter_by(name=item_name).first()
    
    return item_schema.dump(item), 200



# =======================================
# put item information
# =======================================
@item.route('/<string:item_name>', methods=["PUT"])
def put_item(item_name):
    item = ItemModel.query.filter_by(name=item_name).first()
    
    if not item:
        item = ItemModel()
        item.name = item_name
        
    item_json = request.get_json()
    item.price = item_json["price"]
    
    
    try:
        db.session.add(item)
        db.session.commit()
    except Exception as ex:
        return {"message" : f"{ex}"}
    
    return {"message" : "your price of item is update successfully"}
        

# =======================================
# delete item information
# =======================================
@item.route('/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    item = ItemModel.query.filter_by(name=item_name).first()
    
    if not item:
        return {"message" : "this item is not registered yet"}
    
    try:
        db.session.delete(item)
        db.session.commit()
    except Exception as ex:
        return {"message" : f"{ex}"}

    return {"message" : "your item is deleted successfully"}

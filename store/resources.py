from flask_restful import Resource
from flask import request
from .models import StoreModel
from .schemas import StoreSchema
from . import store
from app import db


store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)


# =======================================
# post store 
# =======================================
@store.route('/', methods=['POST'])
def store_post():
    store_json = request.get_json()
    
    store = StoreModel.query.filter_by(name=store_json["name"]).first()
    
    
    if store:
        return {"message":"this store name is already exist"}
    
    store = store_schema.load(store_json)
    
    try:
        db.session.add(store)
        db.session.commit()
    except Exception as ex:
        return {"message" : f"{ex}"}
    
    return store_schema.dump(store), 201


# =======================================
# get store 
# =======================================
@store.route('/<store_name>', methods=['GET'])
def store_get(store_name):
    store = StoreModel.query.filter_by(name=store_name).first()
    if not store:
        return {"message" : "thos store name is not register yet"}
    
    return store_schema.dump(store), 201


# =======================================
# put store 
# =======================================
@store.route('/<string:store_name>', methods=['PUT'])
def store_put(store_name):
    pre_store = StoreModel.query.filter_by(name=store_name).first()
    
    if not pre_store:
        pre_store = StoreModel()
        pre_store.name = store_name
        
    store_json = request.get_json()
    # store = store_schema.load(store_json)
    
    pre_store.name = store_json["name"]
    
    try:
        db.session.add(pre_store)
        db.session.commit()
    except Exception as ex:
        return {"message":f"{ex}"}
    
    return {"message":"your store name is updated"}
    
    
# =======================================
# delete store 
# =======================================
@store.route('/<string:store_name>', methods=['DELETE'])
def store_delete(store_name):
    store = StoreModel.query.filter_by(name=store_name).first()
    
    if not store:
        return {"message":"this name is not set yet"}
    
    store_json = request.get_json()
    store.name = store_json["name"]
    
    try:
        db.session.delete(store)
        db.session.commit()
    except Exception as ex:
        return {"message":f"{ex}"}
    
    return {"message":f"your store by name '{store_name}' is deleted successfully"}

    
    
# =======================================
# get all store 
# =======================================
@store.route('/list', methods=["GET"])
def store_list():
    all_stores = StoreModel.query.all()
    
    return store_list_schema.dump(all_stores), 201
    
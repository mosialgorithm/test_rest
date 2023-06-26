from app import db


class ItemModel(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer(), db.ForeignKey('stores.id'))
    # store = db.relationship("StorModel")
    
    
from app import db 


class StoreModel(db.Model):
    __tablename__ = "stores"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    items = db.relationship('ItemModel', lazy="dynamic")
    
    
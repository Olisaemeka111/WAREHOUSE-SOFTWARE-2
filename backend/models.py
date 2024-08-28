from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(120), nullable=False)
    received_at = db.Column(db.DateTime, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(80), unique=True, nullable=False)
    delivery_info = db.Column(db.String(120), nullable=False)
    items = db.relationship('Item', backref='order', lazy=True)

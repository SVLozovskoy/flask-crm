from app import db
import re

def slugify(lname,fname):
    return str(lname)+str(fname)


class customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    personal_discount = db.Column(db.Integer)
    total  = db.Column(db.Float)

    def __init__(self, *args, **kwarg):
        super(customer, self).__init__(*args, **kwarg)

    def __repr__(self):
        return '< customer id: {} , firstname: {}, lastname: {}>'.format(self.id, self.firstname, self.lastname)


class product(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(150))
    quantity = db.Column(db.Integer)
    article_number = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, *args, **kwarg):
        super(product,self).__init__(*args, **kwarg)


class sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(customer.id))
    product_id = db.Column(db.Integer, db.ForeignKey(product.id))

    def __init__(self, *args, **kwarg):
        super(sale,self).__init__(*args, **kwarg)

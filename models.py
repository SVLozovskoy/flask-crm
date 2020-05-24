from app import db
import re

def slugify(lname,fname):
    return str(lname)+str(fname)


class customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    slug = db.Column(db.String(50), unique = True)

    def __init__(self, *args, **kwarg):
        super(customer, self).__init__(*args, **kwarg)
        self.generate_slug()

    def __repr__(self):
        return '< customer id: {} , firstname: {}, lastname: {}>'.format(self.id, self.firstname, self.lastname)

    def generate_slug(self):
            self.slug = slugify(self.lastname,self.firstname)

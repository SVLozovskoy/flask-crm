from app import app
from app import db
from customers.blueprint import customers
from products.blueprint import  products
import view

app.register_blueprint(customers, url_prefix='/customers')
app.register_blueprint(products, url_prefix='/products')

if __name__ == '__main__':
    app.run()

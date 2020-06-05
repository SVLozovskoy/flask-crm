from app import app
from app import db
from customers.blueprint import customers
from products.blueprint import  products
from sales.blueprint import sales
import view


app.register_blueprint(customers, url_prefix='/customers')
app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(sales, url_prefix='/sales')




if __name__ == '__main__':
    app.run()

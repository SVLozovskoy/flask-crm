from app import app
from app import db
from customers.blueprint import customers
import view

app.register_blueprint(customers, url_prefix='/customers')

if __name__ == '__main__':
    app.run()

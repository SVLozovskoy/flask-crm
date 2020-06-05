from flask import  Blueprint
from flask import  render_template,request,redirect,url_for
from app import db
from models import customer,product
import re

from sqlalchemy import  select
sales = Blueprint('sales', __name__, template_folder='templates')


@sales.route('/main', methods=['GET','POST'])
def displaySales():
    if request.method == 'GET':
        customersList = customer.query.all()
        productList = product.query.all()
        return render_template('sales/main.html', customersList=customersList, productList=productList)
    else:
        customerFull = request.form['f1']
        list= re.split('\s+',customerFull)[1]
    #    id = list[1]
        currentCustomer = db.session.query(customer).filter(customer.id == list)
        productFull = request.form['s2']
        return render_template('sales/test.html', customer = currentCustomer, product = productFull)

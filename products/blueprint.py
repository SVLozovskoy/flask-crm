from flask import  Blueprint
from flask import  render_template,request,redirect,url_for
from models import product as pd
from .forms import ProductForm
from app import db
products = Blueprint('products', __name__, template_folder='templates')

@products.route('/')
def index():
    return render_template('products/index.html')

@products.route('/addProduct', methods = ['GET','POST'])
def addProduct():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
    #    article_number = request.form['article_number']
        quantity = request.form['quantity']

        newProduct = pd(title=title,description=description, quantity=quantity)
        db.session.add(newProduct)
        db.session.commit()

        redirect(url_for('products.index'))
    else:
        form = ProductForm()
        return render_template('products/addProduct.html', form = form)


@products.route('/listOfProducts')
def listOfProducts():
    products = products.query.all()
    return render_template('products/listOfProducts.html', products = products)

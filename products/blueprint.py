from flask import  Blueprint
from flask import  render_template,request,redirect,url_for
from models import product
from .forms import ProductForm
from app import db
products = Blueprint('products', __name__, template_folder='templates')

@products.route('/')
def index():
    return render_template('products/index.html')

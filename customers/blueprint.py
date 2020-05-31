from flask import  Blueprint
from flask import  render_template,request,redirect,url_for
from models import customer
from .forms import CustomerForm
from app import db
customers = Blueprint('customers', __name__, template_folder='templates')


@customers.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lname = request.form['search']
        return redirect(url_for('customers.searsh' ,lname=lname))
    else:
        return render_template('customers/index.html')







@customers.route('/listOfCustomers')
def listOfCustomers():
    customers = customer.query.all()
    return render_template('customers/listOfCustomers.html', customers = customers)

@customers.route('/createCustomer',methods=['GET','POST'])
def createCustomer():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']

        newCustomer = customer(firstname=firstname,lastname=lastname, phone=phone)
        db.session.add(newCustomer)
        db.session.commit()
        return redirect(url_for('customers.index'))
    else:
        form = CustomerForm()
        return render_template('customers/createCustomer.html', form=form)

@customers.route('/customers/<int:id>', methods = ['GET', 'POST'])
def customerDetial(id):
    currentCustomer = customer.query.get(id)
    return render_template('customers/detail.html', customer=currentCustomer)

@customers.route('customers/<int:id>/delete')
def deleteCustomer(id):
    currentCustomer = customer.query.get_or_404(id)
    db.session.delete(currentCustomer)
    db.session.commit()
    return redirect(url_for('customers.listOfCustomers'))

@customers.route('customers/<int:id>/edit',methods=['GET','POST'])
def editCustomer(id):
    currentCustomer = customer.query.get(id)
    if request.method == 'POST':
        currentCustomer.firstname = request.form['firstname']
        currentCustomer.lastname = request.form['lastname']
        currentCustomer.phone = request.form['phone']

        db.session.commit()
        return redirect(url_for('customers.index'))
    else:

        return render_template('customers/editCustomer.html', customer=currentCustomer)


@customers.route('/search/<lname>', methods=['GET', 'POST'])
def searsh(lname):

        list = db.session.query(customer).filter(customer.lastname.like(lname)).all()
        if len(list) == 0:
            return render_template('customers/finder0.html', lname = lname)
        else:
            return render_template('customers/finder.html', list = list, lname = lname)

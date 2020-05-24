from wtforms import Form, StringField,SubmitField



class CustomerForm(Form):
    firstname = StringField('Имя')
    lastname = StringField('Фамилия')
    phone = StringField('Номер телефона')
    submit = SubmitField('Добавить клиента')

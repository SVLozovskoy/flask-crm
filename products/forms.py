from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms import Form

class ProductForm(Form):
    article_number = IntegerField('Артикул товара')
    title = StringField('Название товара')
    description = TextAreaField('Описание товара')
    quantity = IntegerField('Остаток на складе')


    

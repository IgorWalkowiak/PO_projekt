from database import init_db
from flask import Flask, render_template
import credentials
from models import Category, Product
import datetime

app = Flask(__name__)
app.secret_key = credentials.sessionSecretKey
init_db()

@app.route('/')
def home():
    return render_template('template.html', title="Strona główna")

@app.route('/cart')
def cart():
    return render_template('cart.html',
        my_list=[], title="Koszyk")

@app.route('/catalog')
def catalog():
    categories = Category.query.all()
    return render_template('browse_categories.html', categories=categories, title='Kategorie')

@app.route('/category/<category_id>')
def category(category_id):
    prod_in_category = Product.query.filter(Product.category == category_id).all()
    return render_template('browse_category.html', products=prod_in_category, title=f'Kategoria {category_id}')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

from database import init_db
from flask import Flask, render_template, session
import credentials
from models import Category, Product
import frontend_models

app = Flask(__name__)
app.secret_key = credentials.sessionSecretKey
init_db()

@app.route('/x')
def reset():
    session['cart'] = []
    return render_template('template.html', title="Strona główna")


@app.route('/')
def home():
    return render_template('template.html', title="Strona główna")

@app.route('/cart')
def cart():
    try:
        orders = list(set(session['cart']))
        print(orders)
        ordered_products = []
        for order in orders:
            db_product = Product.query.filter(Product.id==order).first()
            order_amount = session['cart'].count(order)
            ordered_products.append(frontend_models.CartProduct(db_product.name, order_amount))
        return render_template('cart.html',
                               products=ordered_products, title="Koszyk")
    except KeyError:
        return render_template('cart.html',
                           products=[], title="Koszyk")

    return render_template('cart.html',
        products=[], title="Koszyk")


@app.route('/catalog')
def catalog():
    categories = Category.query.all()
    return render_template('browse_categories.html', categories=categories, title='Kategorie')

@app.route('/category/<category_id>')
def category(category_id):
    prod_in_category = Product.query.filter(Product.category == category_id).all()
    return render_template('browse_category.html', products=prod_in_category, title=f'Kategoria {category_id}')

@app.route('/product/<product_id>')
def product(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template('browse_product.html', product=product, title=f'{product.name}')

@app.route('/addToCart/<product_id>/<amount>')
def add_to_cart(product_id, amount):
    product_to_cart = Product.query.filter(Product.id == product_id).first()
    for i in range(int(amount)):
        if product_to_cart is not None:
            try:
                    session['cart'] = session['cart'] + [product_id]
            except KeyError:
                    session['cart'] = [product_id]
        print(session['cart'])
    return product(product_id)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

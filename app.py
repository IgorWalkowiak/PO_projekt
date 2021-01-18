from database import init_db, db_session
from flask import Flask, render_template, session, request, jsonify
import credentials
from models import Category, Product, ShopRatings
from product import Product as Prod
from sqlalchemy.sql import func
from cart import Cart

app = Flask(__name__)
app.secret_key = credentials.sessionSecretKey
init_db()

avg_rating = db_session.query(func.avg(ShopRatings.rating).label('average')).first().average
cart_main = Cart()

@app.route('/x')
def reset():
    #session['cart'] = Cart()
    global cart_main
    cart_main = Cart()
    return render_template('template.html', title="Strona główna", avg_rating=avg_rating)


@app.route('/')
def home():
    return render_template('template.html', title="Strona główna", avg_rating=avg_rating)


@app.route('/cart')
def cart():
    global cart_main
    try:
        orders = cart_main.getUnique()
        print(orders)
        ordered_products = []
        for order in orders:
            db_product = Product.query.filter(Product.id == order).first()
            order_amount = cart_main.countProduct(order)
            ordered_products.append(Prod(db_product.name, order_amount, db_product.price))

        sum = 0
        for product in ordered_products:
            db_product = Product.query.filter(Product.name == product.name).first()
            sum = sum + db_product.price * product.amount

        return render_template('cart.html',
                               products=ordered_products, title="Koszyk", price=sum, avg_rating=avg_rating)
    except KeyError:
        return render_template('cart.html',
                           products=[], title="Koszyk", avg_rating=avg_rating)


    return render_template('cart.html',
        products=[], title="Koszyk", avg_rating=avg_rating)


@app.route('/catalog')
def catalog():
    categories = Category.query.all()
    return render_template('browse_categories.html', categories=categories, title='Kategorie', avg_rating=avg_rating)


@app.route('/order_form')
def order_form():
    return render_template('order_form.html', title='Formularz zamówienia', avg_rating=avg_rating)


@app.route('/order', methods=['POST'])
def order():
    global cart_main
    if request.method == 'POST':
        print(request.form)
        delivery_type = request.form['delivery-type']
        try:
            orders = cart_main.getUnique()
            ordered_products = []
            for order in orders:
                db_product = Product.query.filter(Product.id == order).first()
                order_amount = cart_main.countProduct(order)
                ordered_products.append(Prod(db_product.name, order_amount,db_product.price))

            sum = 0
            for product in ordered_products:
                db_product = Product.query.filter(Product.name == product.name).first()
                sum = sum + db_product.price*product.amount
                if product.amount > db_product.amount:
                    raise Exception("Przekroczyłeś produkty w magazynie")

            for product in ordered_products:
                db_product = Product.query.filter(Product.name == product.name).first()
                db_product.amount = db_product.amount - product.amount
                print(db_product.amount)
                db_session.add(db_product)
                db_session.commit()

            cart_main = Cart()
            return render_template('order_result.html', price=sum, avg_rating=avg_rating)

        except KeyError:
            print('error1')

        except Exception as e:
            cart_main = Cart()
            return home()

    return render_template('order_form.html', title='Formularz zamówienia', avg_rating=avg_rating)


@app.route('/category/<category_id>')
def category(category_id):
    prod_in_category = Product.query.filter(Product.category == category_id).all()
    category_name = Category.query.filter(Category.id == category_id).first().name
    return render_template('browse_category.html', products=prod_in_category, title=f'Kategoria {category_name}', avg_rating=avg_rating)


@app.route('/product/<product_id>')
def product(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template('browse_product.html', product=product, title=f'{product.name}', avg_rating=avg_rating)


@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    global cart_main
    if request.method == 'POST':
        product_id = request.form['product_id']
        amount = request.form['quantity']
        product_to_cart = Product.query.filter(Product.id == product_id).first()
        if product_to_cart is not None:
            try:
                    cart_main.add(product_id, amount)
            except KeyError:
                    cart_main = Cart()
                    cart_main.add(product_id, amount)
        return cart()


@app.route('/rate', methods=['POST'])
def rate():
    rating = request.form.get('rate')
    ratingText = request.form.get('text')
    ratingText = None if ratingText == '' else ratingText
    db_session.add(ShopRatings(rating, ratingText))
    db_session.commit()
    global avg_rating
    avg_rating = db_session.query(func.avg(ShopRatings.rating).label('average')).first().average
    return jsonify(status='success')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

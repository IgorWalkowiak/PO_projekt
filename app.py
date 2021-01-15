from database import init_db, db_session
from flask import Flask, render_template, session, request
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
            db_product = Product.query.filter(Product.id == order).first()
            order_amount = session['cart'].count(order)
            ordered_products.append(frontend_models.CartProduct(db_product.name, order_amount))

        sum = 0
        for product in ordered_products:
            db_product = Product.query.filter(Product.name == product.name).first()
            sum = sum + db_product.price * product.amount

        return render_template('cart.html',
                               products=ordered_products, title="Koszyk", price=sum)
    except KeyError:
        return render_template('cart.html',
                           products=[], title="Koszyk")


    return render_template('cart.html',
        products=[], title="Koszyk")


@app.route('/catalog')
def catalog():
    categories = Category.query.all()
    return render_template('browse_categories.html', categories=categories, title='Kategorie')

@app.route('/order_form')
def order_form():
    return render_template('order_form.html', title='Formularz zamówienia')

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        print(request.form)
        delivery_type = request.form['delivery-type']
        try:
            orders = list(set(session['cart']))
            ordered_products = []
            for order in orders:
                db_product = Product.query.filter(Product.id == order).first()
                order_amount = session['cart'].count(order)
                ordered_products.append(frontend_models.CartProduct(db_product.name, order_amount))

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


            session['cart']=[]
            return render_template('order_result.html', price=sum)

        except KeyError:
            print('error1')

        except Exception as e:
            session['cart'] = []
            return home()

    return render_template('order_form.html', title='Formularz zamówienia')

@app.route('/category/<category_id>')
def category(category_id):
    prod_in_category = Product.query.filter(Product.category == category_id).all()
    return render_template('browse_category.html', products=prod_in_category, title=f'Kategoria {category_id}')

@app.route('/product/<product_id>')
def product(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template('browse_product.html', product=product, title=f'{product.name}')

@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        amount = request.form['quantity']
        product_to_cart = Product.query.filter(Product.id == product_id).first()
        for i in range(int(amount)):
            if product_to_cart is not None:
                try:
                        session['cart'] = session['cart'] + [product_id]
                except KeyError:
                        session['cart'] = [product_id]
        return cart()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

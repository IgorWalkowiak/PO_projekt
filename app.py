from models.database import init_db, db_session
from flask import Flask, render_template, session, request, jsonify
import credentials
from models.models import Category, Product, ShopRatings
from models.product import Product as Prod
from sqlalchemy.sql import func
from models.cart import Cart
from controllers.controller import Controller


app = Flask(__name__)
app.secret_key = credentials.sessionSecretKey
controller = Controller(session)


@app.route('/x')
def reset():
    return controller.reset()


@app.route('/')
def home():
    return controller.home()


@app.route('/cart')
def cart():
    return controller.cart()


@app.route('/catalog')
def catalog():
    return controller.catalog()


@app.route('/order_form')
def order_form():
    return controller.order_form()


@app.route('/order', methods=['POST'])
def order():
    return controller.order(request)


@app.route('/category/<category_id>')
def category(category_id):
    return controller.category(category_id)


@app.route('/product/<product_id>')
def product(product_id):
    return controller.product(product_id)


@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    return controller.add_to_cart(request)


@app.route('/rate', methods=['POST'])
def rate():
    return controller.rate(request)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

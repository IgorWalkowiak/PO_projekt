from models.database import init_db, db_session
from models.models import Category, Product, ShopRatings
from models.product import Product as Prod
from sqlalchemy.sql import func
from models.cart import Cart
from flask import jsonify, render_template


class Controller:
  avg_rating = db_session.query(func.avg(ShopRatings.rating).label('average')).first().average
  cart_main = Cart()

  def __init__(self):
    init_db()


  def reset(self):
      self.cart_main = Cart()
      return render_template('template.html', title="Strona główna", avg_rating=self.avg_rating)


  def home(self):
    return render_template('template.html', title="Strona główna", avg_rating=self.avg_rating)


  def cart(self):
    try:
        orders = self.cart_main.getUnique()
        print(orders)
        ordered_products = []
        for order in orders:
            db_product = Product.query.filter(Product.id == order).first()
            order_amount = self.cart_main.countProduct(order)
            ordered_products.append(Prod(db_product.name, order_amount, db_product.price))

        sum = 0
        for product in ordered_products:
            db_product = Product.query.filter(Product.name == product.name).first()
            sum = sum + db_product.price * product.amount

        return render_template('cart.html',
                               products=ordered_products, title="Koszyk", price=sum, avg_rating=self.avg_rating)
    except KeyError:
        return render_template('cart.html',
                           products=[], title="Koszyk", avg_rating=self.avg_rating)
    return render_template('cart.html',
        products=[], title="Koszyk", avg_rating=self.avg_rating)


  def catalog(self):
    categories = Category.query.all()
    return render_template('browse_categories.html', categories=categories, title='Kategorie', avg_rating=self.avg_rating)


  def order_form(self):
    return render_template('order_form.html', title='Formularz zamówienia', avg_rating=self.avg_rating)


  def order(self, request):
    if request.method == 'POST':
        print(request.form)
        delivery_type = request.form['delivery-type']
        try:
            orders = self.cart_main.getUnique()
            ordered_products = []
            for order in orders:
                db_product = Product.query.filter(Product.id == order).first()
                order_amount = self.cart_main.countProduct(order)
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

            self.cart_main = Cart()
            return render_template('order_result.html', price=sum, avg_rating=self.avg_rating)

        except KeyError:
            print('error1')

        except Exception as e:
            self.cart_main = Cart()
            return render_template('template.html',
              title="Nie można stworzyć zamówienia, przekroczyłeś liczbę produktów w magazynie",
              avg_rating=self.avg_rating)

    return render_template('order_form.html', title='Formularz zamówienia', avg_rating=self.avg_rating)


  def category(self, category_id):
    prod_in_category = Product.query.filter(Product.category == category_id).all()
    category_name = Category.query.filter(Category.id == category_id).first().name
    return render_template('browse_category.html', products=prod_in_category, title=f'Kategoria {category_name}', avg_rating=self.avg_rating)


  def product(self, product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template('browse_product.html', product=product, title=f'{product.name}', avg_rating=self.avg_rating)


  def add_to_cart(self, request):
    if request.method == 'POST':
        product_id = request.form['product_id']
        amount = request.form['quantity']
        product_to_cart = Product.query.filter(Product.id == product_id).first()
        if product_to_cart is not None:
            try:
                    self.cart_main.add(product_id, amount)
            except KeyError:
                    self.cart_main = Cart()
                    self.cart_main.add(product_id, amount)
        return self.cart()


  def rate(self, request):
    rating = request.form.get('rate')
    ratingText = request.form.get('text')
    ratingText = None if ratingText == '' else ratingText
    db_session.add(ShopRatings(rating, ratingText))
    db_session.commit()
    self.avg_rating = db_session.query(func.avg(ShopRatings.rating).label('average')).first().average
    return jsonify(status='success')

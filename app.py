from database import init_db
from flask import Flask, render_template
import credentials

app = Flask(__name__)
app.secret_key = credentials.sessionSecretKey
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/catalog')
def catalog():
    return render_template('browse_categories.html')


if __name__ == '__main__':
    app.run()
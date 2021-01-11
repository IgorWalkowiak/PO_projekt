from models import Category,Product
from database import init_db, db_session

init_db()


Product.query.delete(synchronize_session=False)
db_session.commit()
Category.query.delete(synchronize_session=False)
db_session.commit()


categories = ["Pralki", "Zmywarki", "Lodówki", "Piekarniki", "Mikrofale"]
products = [
    (1, "EXPRESS Pralka", "Opis pralki", 6, 2),
    (1, "Super zmywarka 20k", "Opis zmywarki", 9, 1),
    (2, "Lodówka 3000", "Opis lodówki", 53, 6)
]






for category in categories:
    cat = Category(category)
    db_session.add(cat)
    db_session.commit()

for product in products:
    prod = Product(product[0], product[1], product[2], product[3], product[4])
    db_session.add(prod)
    db_session.commit()
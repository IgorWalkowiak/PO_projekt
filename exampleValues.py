from models import Category,Product
from database import init_db, db_session

init_db()


Product.query.delete(synchronize_session=False)
db_session.commit()
#Category.query.delete(synchronize_session=False)
#db_session.commit()


categories = ["Pralki", "Zmywarki", "Lodówki", "Piekarniki", "Mikrofale"]
products = [
    (1, "EXPRESS Pralka", "Opis pralki", 200, 2),
    (1, "Samsung QuickDrive", "Opis pralki", 250, 1),
    (1, "Whirlpool FFB ", "Opis pralki", 2000, 6),
    (1, "Electrolux PerfectCare", "Opis pralki", 500, 6),
    (1, "LG Vivace", "Opis pralki", 400, 10),
    (2, "Super zmywarka 20k", "Opis zmywarki", 500, 2),
    (2, "Zmywarka LG", "Opis zmywarki", 250, 7),
    (3, "Lodówka 3000", "Opis lodówki", 350, 8),
    (3, "Lodówka Beko", "Opis lodówki", 3000, 4),
    (4, "Piekarniki LG", "Opis piekarnika", 400, 3),
    (5, "Mikrofala SAMSUNG", "Opis mikrofali", 450, 6)
]






for category in categories:
    cat = Category(category)
    db_session.add(cat)
    db_session.commit()

for product in products:
    prod = Product(product[0], product[1], product[2], product[3], product[4])
    db_session.add(prod)
    db_session.commit()
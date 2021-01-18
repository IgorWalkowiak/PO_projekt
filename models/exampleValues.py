from models import Category, Product, ShopRatings
from database import init_db, db_session


init_db()


Product.query.delete(synchronize_session=False)
db_session.commit()
# Category.query.delete(synchronize_session=False)
# db_session.commit()


categories = ["Pralki", "Zmywarki", "Lodówki", "Piekarniki", "Mikrofale"]
products = [
    (1, "EXPRESS Pralka", "Opis pralki", 200, 20),
    (1, "Samsung QuickDrive", "Opis pralki", 250, 10),
    (1, "Whirlpool FFB ", "Opis pralki", 2000, 25),
    (1, "Electrolux PerfectCare", "Opis pralki", 500, 26),
    (1, "LG Vivace", "Opis pralki", 400, 11),
    (2, "Super zmywarka 20k", "Opis zmywarki", 500, 12),
    (2, "Zmywarka LG", "Opis zmywarki", 250, 71),
    (3, "Lodówka 3000", "Opis lodówki", 350, 82),
    (3, "Lodówka Beko", "Opis lodówki", 3000, 41),
    (4, "Piekarniki LG", "Opis piekarnika", 400, 31),
    (5, "Mikrofala SAMSUNG", "Opis mikrofali", 450, 65)
]
ratings = [
    (3, "Slaby"),
    (2, None),
    (5, "Bardzo dobry sklep"),
    (2, None)
]

for category in categories:
    cat = Category(category)
    db_session.add(cat)
    db_session.commit()

for product in products:
    prod = Product(product[0], product[1], product[2], product[3], product[4])
    db_session.add(prod)
    db_session.commit()

for rating in ratings:
    rat = ShopRatings(rating[0], rating[1])
    db_session.add(rat)
    db_session.commit()

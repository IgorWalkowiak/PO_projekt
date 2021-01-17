from sqlalchemy import Column, Integer, String
from database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    category = Column(Integer)
    name = Column(String(100))
    description = Column(String(1000))
    price = Column(Integer)
    amount = Column(Integer)


    def __init__(self, category=None, name=None, description=None, price=None, amount=None):
        self.category = category
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount


    def __repr__(self):
        return '<Product %r>' % (self.name)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


    def __init__(self, name=None):
        self.name = name


    def __repr__(self):
        return '<catalog %r>' % (self.name)


class ShopRatings(Base):
    __tablename__ = 'shop_ratings'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    description = Column(String(100))


    def __init__(self, rating=None, description=None):
        self.rating = rating
        self.description = description


    def __repr__(self):
        return '<Rating %r>' % (self.rating)

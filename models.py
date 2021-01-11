from sqlalchemy import Column, Integer, String
from database import Base



class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))
    price = Column(Integer)
    amount = Column(Integer)

    def __init__(self, name=None, description=None, price=None, amount=None):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount

    def __repr__(self):
        return '<Product %r>' % (self.name)


class catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<catalog %r>' % (self.name)

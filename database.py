import credentials
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, ForeignKey

engine = create_engine('mysql://{}:{}@{}/shop'.format(credentials.login, credentials.password, credentials.host_address))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
meta = MetaData()

products = Table(
   'products', meta,
   Column('id', Integer, primary_key=True),
   Column('category', Integer, ForeignKey("categories.id"), nullable=False),
   Column('name', String(100), nullable=False),
   Column('description', String(1000), nullable=False),
   Column('price', Integer, nullable=False),
   Column('amount', Integer, nullable=False)
)

category = Table(
   'categories', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(100), nullable=False)
)

ratings = Table(
   'shop_ratings', meta,
   Column('id', Integer, primary_key=True),
   Column('rating', Integer),
   Column('description', String(100))
)

meta.create_all(engine)


def init_db():
    import models
    Base.metadata.create_all(bind=engine)

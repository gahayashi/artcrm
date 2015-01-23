from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, Index
from sqlalchemy.sql.sqltypes import Integer, Text
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension = ZopeTransactionExtension()))
Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique = True, mysql_length = 255)

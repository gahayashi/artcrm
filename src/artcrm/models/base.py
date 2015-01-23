# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import declared_attr
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, Index
from sqlalchemy.sql.sqltypes import Integer, Text
from zope.sqlalchemy import ZopeTransactionExtension


class BaseObject(object):
    '''All objects in this application inherit from this class'''

DBSession = scoped_session(sessionmaker(extension = ZopeTransactionExtension()))
Base = declarative_base(cls = BaseObject)

class BaseModel(object):
    @declared_attr
    def __tablename__(cls): # @NoSelf
        return '%ss' % cls.__name__.lower()

    # --- Generic Model Fields ---
    id = Column(Integer, primary_key = True)

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique = True, mysql_length = 255)

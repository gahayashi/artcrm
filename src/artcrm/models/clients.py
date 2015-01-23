# -*- coding: utf-8 -*-
'''
Created on Jan 23, 2015
@author: Gabriele Hayashi
'''
from sqlalchemy.orm.mapper import validates
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Unicode, String

from artcrm import validators
from artcrm.models import Base, BaseModel


class Client(Base, BaseModel):
    # --- Personal Information ---
    first_name = Column(Unicode(128))
    last_name = Column(Unicode(128))

    # --- Contact Information ---
    email = Column(Unicode(120), unique = True, nullable = True)
    phone = Column(String(len('+99 99 9-9999-9999')), nullable = True)
    mobile = Column(String(len('+99 99 9-9999-9999')), nullable = True)

    @validates('email')
    def validates_email(self, name, email):
        return validators.email(name, email)

    @validates('phone', 'mobile')
    def validates_phones(self, name, phone):
        return validators.phone(name, phone)

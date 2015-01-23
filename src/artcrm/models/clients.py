# -*- coding: utf-8 -*-
'''
Created on Jan 23, 2015
@author: Gabriele Hayashi
'''
from datetime import datetime

from pyramid.i18n import TranslationStringFactory
from sqlalchemy.orm.mapper import validates
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Unicode, String, Enum, Date, DateTime, \
    UnicodeText, Boolean

from artcrm import validators
from artcrm.models import Base, BaseModel


_ = TranslationStringFactory('artcrm')

class Client(Base, BaseModel):
    # --- Personal Information ---
    first_name = Column(Unicode(128))
    last_name = Column(Unicode(128))
    birth = Column(Date, nullable = True)

class ClientPhone(Base, BaseModel):
    MOBILE, HOME, WORK, FAX = 'm', 'h', 'w', 'f'
    TYPES = {
        MOBILE: _('mobile'),
        HOME: _('home'),
        WORK: _('work'),
        FAX: _('fax')
    }

    # --- Relation ---
    id_client = Column(ForeignKey(Client.id))

    # --- Data ---
    number = Column(String(len('+99 99 9-9999-9999')), nullable = True)
    type = Column(Enum(TYPES.keys()))
    carrier = Column(Unicode(64))

    @validates('number')
    def validates_phones(self, name, phone):
        return validators.phone(name, phone)

class ClientEmail(Base, BaseModel):
    HOME, WORK = 'h', 'w'
    TYPES = {
        HOME: _('home'),
        WORK: _('work')
    }

    # --- Relation ---
    id_client = Column(ForeignKey(Client.id))

    # --- Data ---
    email = Column(Unicode(120), unique = True)
    type = Column(Enum(TYPES.keys()))

    @validates('email')
    def validates_email(self, name, email):
        return validators.email(name, email)

class ClientLog(Base, BaseModel):
    # --- Admin ---
    timestamp = Column(DateTime, default = datetime.now)
    is_active = Column(Boolean, default = True)

    # --- Information ---
    text = Column(UnicodeText)
    id_client = Column(ForeignKey(Client.id))

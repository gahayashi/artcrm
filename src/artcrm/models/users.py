# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
from datetime import datetime
import re

from cryptacular.core import DelegatingPasswordManager
from cryptacular.pbkdf2 import PBKDF2PasswordManager
from pyramid.i18n import TranslationStringFactory
from sqlalchemy.ext.declarative.api import declared_attr
from sqlalchemy.orm import synonym
from sqlalchemy.orm.mapper import validates
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Unicode, Boolean, DateTime

from artcrm.models import DBSession
from artcrm.models.base import Base, BaseModel


_ = TranslationStringFactory('artcrm')
pwman = DelegatingPasswordManager(
    preferred = PBKDF2PasswordManager()
)

class Autheticatable(object):
    # --- Account Information ---
    email = Column(Unicode(120), unique = True)
    _password = Column(Unicode(140))

    # --- Special Accounts ---
    verified = Column(Boolean, default = False)

    # --- Administration ---
    date_joined = Column(DateTime, default = datetime.now)
    last_login = Column(DateTime, default = datetime.now)
    is_admin = Column(Boolean, default = False)
    is_staff = Column(Boolean, default = False)
    is_active = Column(Boolean, default = False)

    # --- Constants ---
    is_authenticated = True

    def set_password(self, password):
        self._password = pwman.encode(password)
        return self._password
    def get_password(self):
        return self._password
    def check_password(self, password):
        return pwman.check(self._password, password,
            lambda password: self.set_password(password)
        )

    @declared_attr
    def password(cls): # @NoSelf
        return synonym('_password',
            descriptor = property(
                cls.get_password,
                cls.set_password
            )
        )

    @validates('email')
    def validates_email(self, name, email):
        assert re.match('[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+', email), _(
            'error-validates-email',
            default = 'This field does not look like an email address'
        )
        return email

    class AnonymousUser(object):
        def __getattr__(self, name):
            return None
        is_authenticated = False
        def check_password(self, password):
            return False

    @classmethod
    def get_user(cls, request):
        if not hasattr(request, '_user'):
            session = DBSession()
            userid = request.unauthenticated_userid
            request._user = session.query(cls).get(userid) if userid else cls.AnonymousUser()
        return request._user

class User(Base, BaseModel, Autheticatable):
    pass

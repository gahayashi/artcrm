# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
import unittest

from pyramid import testing
from sqlalchemy.engine import create_engine
import transaction

from artcrm.models import DBSession, Base, MyModel


class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        engine = create_engine('sqlite://')
        DBSession.configure(bind = engine)
        Base.metadata.create_all(engine) # @UndefinedVariable
        with transaction.manager:
            model = MyModel(name = 'one', value = 55)
            DBSession.add(model) # @UndefinedVariable

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

class TestMyViewFailureCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        engine = create_engine('sqlite://')
        DBSession.configure(bind = engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

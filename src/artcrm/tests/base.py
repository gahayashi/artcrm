import unittest

from pyramid import testing
from sqlalchemy.engine import create_engine
import transaction

from artcrm.models import DBSession, Base, MyModel
from artcrm.views.base import my_view


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

    def test_passing_view(self):
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'artcrm')


class TestMyViewFailureCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        engine = create_engine('sqlite://')
        DBSession.configure(bind = engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_failing_view(self):
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info.status_int, 500)

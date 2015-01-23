# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
import os
import sys

from pyramid.paster import setup_logging, get_appsettings
from pyramid.scripts.common import parse_vars
from sqlalchemy import engine_from_config
import transaction

from artcrm.models import DBSession, Base, MyModel


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv = sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options = options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind = engine)
    Base.metadata.create_all(engine) # @UndefinedVariable
    with transaction.manager:
        model = MyModel(name = 'one', value = 1)
        DBSession.add(model) # @UndefinedVariable

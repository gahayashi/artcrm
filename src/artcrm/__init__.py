# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from artcrm.models import DBSession, Base


def main(global_config, **settings):
    # --- Database ---
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind = engine)
    Base.metadata.bind = engine

    # --- Configuration ---
    config = Configurator(settings = settings)

    # --- Inclusions ---
    map(config.include, [
        'pyramid_jinja2'
    ])

    # --- Routes ---
    config.add_static_view('static', 'static', cache_max_age = 3600)
    config.add_route('home', '/')

    # --- App ---
    config.scan()
    return config.make_wsgi_app()

# -*- coding: utf-8 -*-
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from artcrm.models import DBSession, Base


VERSION = (0, 1, 0)
version = '.'.join(str(i) for i in VERSION)


def admin_views(config):
    config.add_route('web:admin', '')
def public_views(config):
    config.add_route('web:root', '')

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
    config.include(public_views)
    config.include(admin_views, 'admin')

    # --- Request Methods ---
    config.add_request_method('artcrm.models.users.User.get_user', 'user', reify = True)
    def sitesettings(*args, **kwargs):
        site = {
            'name' : 'ArtCRM',
            'version' : version,
            'author' : 'John Doe',
            'background' : 'http://localhost/~gabriele/bg.jpeg'
        }
        site.update(settings)
        return site
    config.add_request_method(sitesettings, 'site', reify = True)

    # --- App ---
    config.scan()
    return config.make_wsgi_app()

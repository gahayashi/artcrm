# -*- coding: utf-8 -*- 
'''
Created on Jan 22, 2015
@author: Gabriele Hayashi
'''
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    
    'cryptacular',
]

entry_points = """
    [paste.app_factory]
    main = artcrm:main
    [console_scripts]
    initialize_artcrm_db = artcrm.scripts.initializedb:main
"""

setup(
    name = 'artcrm',
    version = '0.0',
    description = 'artcrm',
    long_description = README + '\n\n' + CHANGES,
    classifiers = [
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author = 'Gabriele Hayashi',
    author_email = 'gabriele.hayashi@gmail.com',
    url = '',
    keywords = 'web wsgi bfg pylons pyramid',
    packages = find_packages('src'),
    package_dir = {'' : 'src'},
    include_package_data = True,
    zip_safe = False,
    test_suite = 'artcrm',
    install_requires = requires,
    entry_points = entry_points
)

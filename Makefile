# 
# ArtCRM makefile
# common targets for the artcrm project
# 

SHELL := /bin/bash

develop install:
	pip install -r requirements.txt
	python setup.py "$@"

# --- Development targets --- 
# Usually this commands should not be called in a production environment.
# (except for the db, but it should be called all the time...)
serve:
	pserve --reload development.ini
routes:
	proutes development.ini
db:
	initialize_artcrm_db development.ini

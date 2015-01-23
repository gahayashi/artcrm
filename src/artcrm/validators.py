# -*- coding: utf-8 -*-
'''
Created on Jan 23, 2015
@author: Gabriele Hayashi
'''
import re

from pyramid.i18n import TranslationStringFactory


_ = TranslationStringFactory('artcrm')

def email(name, email):
    assert re.match('[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+', email), _(
        'error-validates-email',
        default = 'This field does not look like an email address'
    )
    return email

def phone(name, phone):
    assert re.match('[0-9+()]+', phone), _(
        'error-validates-phone',
        default = 'This field does not look like a phone number'
    )
    return phone

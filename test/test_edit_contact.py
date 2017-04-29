# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact()



# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_group(app):
    app.group.edit_first_group()

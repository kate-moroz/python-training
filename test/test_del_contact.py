# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(fname = "test", mname = "test1", lname="test2"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)




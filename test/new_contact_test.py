# -*- coding: utf-8 -*-
import pytest

from fixture.application_contact import Application_contact
from model.contact import Contact


@pytest.fixture
def application(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy_page)
    return fixture


def test_new_contact_test(application):
    application.login(username="admin", password="secret")
    application.create_contact(Contact(fname="somename", mname="somemname", lname="somelname", nname="somenickname", title="sometitle", company="somecompany",
                        address1="someaddress1", homenum="somehomenumber", mobnum="somemobilenumber", worknum="someworknumber", fax="somefax",
                        email1="someemail", email2="someemail2", email3="someemail3", homepage="somehomepage", birthyear="1990", anniversary="2000", address2="someaddress2",
                        notes="somenotes"))
    application.logout()



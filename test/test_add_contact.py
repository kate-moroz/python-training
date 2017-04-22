# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(fname="somename", mname="somemname", lname="somelname", nname="somenickname", title="sometitle", company="somecompany",
                               address1="someaddress1", homenum="somehomenumber", mobnum="somemobilenumber", worknum="someworknumber", fax="somefax",
                               email1="someemail", email2="someemail2", email3="someemail3", homepage="somehomepage", birthyear="1990", anniversary="2000", address2="someaddress2",
                               notes="somenotes"))
    app.session.logout()


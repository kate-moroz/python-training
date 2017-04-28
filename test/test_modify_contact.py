from model.contact import Contact


def test_modify_contact_fname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(fname="New First Name"))
    app.session.logout()

def test_modify_contact_mname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mname="New Middle Name"))
    app.session.logout()

def test_modify_contact_lname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lname="New Last Name"))
    app.session.logout()
from model.contact import Contact


def test_modify_contact_fname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(fname = "test", mname = "test1", lname="test2"))
    app.contact.modify_first_contact(Contact(fname="New First Name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    
#def test_modify_contact_mname(app):
#    app.contact.modify_first_contact(Contact(mname="New Middle Name"))

#def test_modify_contact_lname(app):
#    app.contact.modify_first_contact(Contact(lname="New Last Name"))

from model.contact import Contact


def test_delete_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(lastname="tmp"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    del old_contacts[0]
    assert old_contacts == new_contacts

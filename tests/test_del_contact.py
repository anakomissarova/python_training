from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(lastname="tmp"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    del old_contacts[index]
    assert old_contacts == new_contacts

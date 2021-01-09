from model.contact import Contact
from random import randrange


def test_edit_contact(app, data_constant_contacts):
    if not app.contact.count():
        app.contact.create(Contact(firstname="tmp"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    new_contact = data_constant_contacts
    new_contact.contact_id = old_contacts[index].contact_id
    app.contact.edit_contact_by_index(index, new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.compare_ids) == sorted(new_contacts, key=Contact.compare_ids)

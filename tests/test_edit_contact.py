from model.contact import Contact


def test_edit_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(firstname="tmp"))
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Firstname 1", lastname="Lastname")
    new_contact.contact_id = old_contacts[0].contact_id
    app.contact.edit_first_contact(new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contact.compare_ids) == sorted(new_contacts, key=Contact.compare_ids)

from model.contact import Contact


def test_add_contact(app, json_random_contacts):
    contact = json_random_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.compare_ids) == \
           sorted(new_contacts, key=Contact.compare_ids)

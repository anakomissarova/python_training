from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname='test firstname', lastname='test lastname', mobile='+78943562435')
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.compare_ids) == \
           sorted(new_contacts, key=Contact.compare_ids)






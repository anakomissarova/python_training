from model.contact import Contact
import random


def test_edit_contact(app, db, data_constant_contacts, check_ui):
    if not app.contact.count():
        app.contact.create(Contact(firstname="tmp"))
    old_contacts = db.get_contacts_list()
    new_contact = data_constant_contacts
    new_contact.contact_id = random.choice(old_contacts).contact_id
    app.contact.edit_contact_by_id(new_contact)
    new_contacts = db.get_contacts_list()
    for contact in old_contacts:
        if contact.contact_id == new_contact.contact_id:
            old_contacts.remove(contact)
            break
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.compare_ids) == sorted(new_contacts, key=Contact.compare_ids)
    if check_ui:
        assert sorted(map(app.contact.clear_name_from_spaces, new_contacts), key=Contact.compare_ids) == \
               sorted(app.contact.get_contacts_list(), key=Contact.compare_ids)

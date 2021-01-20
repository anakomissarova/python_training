from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if not app.contact.count():
        app.contact.create(Contact(lastname="tmp"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    # TODO: add assertion that contact is deleted from groups as well
    if check_ui:
        assert sorted(map(app.contact.clear_name_from_spaces, new_contacts), key=Contact.compare_ids) == \
               sorted(app.contact.get_contacts_list(), key=Contact.compare_ids)

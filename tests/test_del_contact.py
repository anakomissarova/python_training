from model.contact import Contact
import random
import allure


def test_delete_contact(app, db, check_ui):
    with allure.step('Given non-empty list of contacts'):
        if not app.contact.count():
            app.contact.create(Contact(lastname="tmp"))
        old_contacts = db.get_contacts_list()
        contact = random.choice(old_contacts)
    with allure.step('When I delete a random contact %s' % contact):
        app.contact.delete_contact_by_id(contact)
    with allure.step('Then the new list of contacts is equal to the old list with the contact removed'):
        new_contacts = db.get_contacts_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(map(app.contact.clear_name_from_spaces, new_contacts), key=Contact.compare_ids) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.compare_ids)

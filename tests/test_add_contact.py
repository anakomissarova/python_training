from model.contact import Contact
import allure


def test_add_contact(app, db, json_random_contacts, check_ui):
    contact = json_random_contacts
    with allure.step('Given A list of contacts'):
        old_contacts = db.get_contacts_list()
    with allure.step('When I add contact %s to the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new list of contacts is equal to the old list with a new contact added'):
        new_contacts = db.get_contacts_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.compare_ids) == \
               sorted(new_contacts, key=Contact.compare_ids)
        if check_ui:
            assert sorted(map(app.contact.clear_name_from_spaces, new_contacts), key=Contact.compare_ids) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.compare_ids)

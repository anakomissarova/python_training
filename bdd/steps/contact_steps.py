from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a list of contacts', target_fixture='contacts_list')
def contacts_list(db):
    return db.get_contacts_list()


@given('a new contact with <firstname>, <lastname> and <mobile_phone>', target_fixture='new_contact')
@given('new contact data: <firstname>, <lastname> or <mobile_phone>', target_fixture='new_contact')
def new_contact(firstname, lastname, mobile_phone):
    return Contact(firstname=firstname, lastname=lastname, mobile=mobile_phone)


@given('a random contact from the list', target_fixture='random_contact')
def choose_random_contact(nonempty_contacts_list):
    return random.choice(nonempty_contacts_list)


@given('non-empty list of contacts',  target_fixture='nonempty_contacts_list')
def nonempty_contacts_list(app, db):
    if not app.contact.count():
        app.contact.create(Contact(lastname="tmp"))
    return db.get_contacts_list()


@when('I add new contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@when('I delete the contact')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact)


@when('I edit the contact')
def edit_contact(app, random_contact, new_contact):
    new_contact.contact_id = random_contact.contact_id
    app.contact.edit_contact_by_id(new_contact)


@then('the new list of contacts is equal to the old list with a new contact added')
def verify_contact_added(db, contacts_list, new_contact):
    old_list = contacts_list
    new_list = db.get_contacts_list()
    old_list.append(new_contact)
    assert sorted(old_list, key=Contact.compare_ids) == \
           sorted(new_list, key=Contact.compare_ids)


@then('the new list of contacts is equal to the old list with modified contact replaced')
def verify_contact_modified(db, nonempty_contacts_list, new_contact):
    old_list = nonempty_contacts_list
    new_list = db.get_contacts_list()
    for contact in old_list:
        if contact.contact_id == new_contact.contact_id:
            old_list.remove(contact)
            break
    old_list.append(new_contact)
    assert sorted(old_list, key=Contact.compare_ids) == \
           sorted(new_list, key=Contact.compare_ids)


@then('the new list of contacts is equal to the old list with the contact removed')
def verify_contact_deleted(db, nonempty_contacts_list, random_contact):
    old_list = nonempty_contacts_list
    new_list = db.get_contacts_list()
    old_list.remove(random_contact)
    assert sorted(old_list, key=Contact.compare_ids) == \
           sorted(new_list, key=Contact.compare_ids)

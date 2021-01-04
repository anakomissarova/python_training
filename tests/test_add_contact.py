from model.contact import Contact
import pytest
from random import randrange, choices
from string import ascii_letters, digits, punctuation


def random_string(prefix, maxlen):
    chars = ascii_letters + digits + punctuation + " "*10
    return prefix + "".join(choices(chars, k=randrange(maxlen)))


test_data = [
    Contact(firstname=random_string("first", 10), lastname=random_string("last", 10), mobile=random_string("", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(i) for i in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.compare_ids) == \
           sorted(new_contacts, key=Contact.compare_ids)

import re
from random import randrange


def test_info_on_homepage(app, db):
    contacts_from_homepage = sorted(app.contact.get_contacts_list(), key=lambda c: c.contact_id)
    contacts_from_db = sorted(db.get_contacts_list(), key=lambda c: c.contact_id)
    for i in range(len(contacts_from_homepage)):
        assert contacts_from_homepage[i].lastname == contacts_from_db[i].lastname.rstrip()
        assert contacts_from_homepage[i].firstname == contacts_from_db[i].firstname.rstrip()
        assert contacts_from_homepage[i].address == clear_address(contacts_from_db[i].address)
        assert contacts_from_homepage[i].emails_from_homepage == merge_emails_like_homepage(contacts_from_db[i])
        assert contacts_from_homepage[i].phones_from_homepage == merge_phones_like_homepage(contacts_from_db[i])


def test_phones_on_contact_view(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work


def clear_phone(s):
    return re.sub("[() -]", "", s)


def clear_address(s):
    return re.sub(" \n", "\n", s.replace("\r\n", "\n"))


def merge_phones_like_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.secondary]))))


def merge_emails_like_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(str.strip,
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))

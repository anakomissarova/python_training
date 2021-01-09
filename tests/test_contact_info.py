import re
from random import randrange


def test_info_on_homepage(app):
    index = randrange(app.contact.count())
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    # check lastname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname.rstrip()
    # check firstname
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname.rstrip()
    # check address
    assert contact_from_homepage.address == clear_address(contact_from_edit_page.address)
    # check e-mails
    assert contact_from_homepage.emails_from_homepage == merge_emails_like_homepage(contact_from_edit_page)
    # check phones
    assert contact_from_homepage.phones_from_homepage == merge_phones_like_homepage(contact_from_edit_page)


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
    return re.sub(" \n", "\n", s)


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

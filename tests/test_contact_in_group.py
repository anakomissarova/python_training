from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, orm):
    if orm.count_contacts() == 0:
        app.contact.create(Contact(firstname='Ivan', lastname='Ivanov'))
    contact = random.choice(orm.get_contacts_list())
    old_groups = orm.get_groups_for_contact(contact)
    if orm.count_groups() == 0 or orm.count_groups() <= len(old_groups):
        app.group.create(Group(name='new group'))
    available_groups = set(orm.get_groups_list()).difference(old_groups)
    group = random.choice(list(available_groups))
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    old_groups.append(group)
    old_contacts.append(contact)
    new_groups = orm.get_groups_for_contact(contact)
    new_contacts = orm.get_contacts_in_group(group)
    assert old_groups == new_groups
    assert old_contacts == new_contacts


def test_delete_contact_from_group(app, orm):
    if orm.count_contacts_and_groups_links() == 0:
        if orm.count_groups() == 0:
            app.group.create(Group(name='new group'))
        if orm.count_contacts() == 0:
            app.contact.create(Contact(firstname='Ivan', lastname='Ivanov'))
        contact = random.choice(orm.get_contacts_list())
        group = random.choice(orm.get_groups_list())
        app.contact.add_contact_to_group_by_id(contact, group)
    group = orm.get_first_group_with_contacts()
    old_contacts = orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts)
    old_groups = orm.get_groups_for_contact(contact)
    app.contact.delete_contact_from_group(contact=contact, group=group)
    old_groups.remove(group)
    old_contacts.remove(contact)
    new_groups = orm.get_groups_for_contact(contact)
    new_contacts = orm.get_contacts_in_group(group)
    assert old_groups == new_groups
    assert old_contacts == new_contacts

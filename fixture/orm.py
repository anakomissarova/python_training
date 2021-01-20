from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    def __init__(self, host, dbname, user, password):
        self.db.bind(provider='mysql', host=host, db=dbname, user=user, passwd=password)
        self.db.generate_mapping()
        # sql_debug(True)

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        group_id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set('ORMContact', table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        contact_id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set('ORMGroup', table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    @db_session
    def get_groups_list(self):
        return self.convert_groups(select(g for g in self.ORMGroup))

    def convert_groups(self, orm_groups):
        def convert(group):
            return Group(group_id=str(group.group_id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, orm_groups))

    @db_session
    def count_groups(self):
        return select(g for g in self.ORMGroup).count()

    @db_session
    def get_contacts_list(self):
        return self.convert_contacts(select(c for c in self.ORMContact if c.deprecated is None))

    def convert_contacts(self, orm_contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.contact_id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, orm_contacts))

    @db_session
    def count_contacts(self):
        return select(c for c in self.ORMContact).count()

    def select_group_by_id(self, group_id):
        return list(select(g for g in self.ORMGroup if g.group_id == group_id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.select_group_by_id(group.group_id)
        return self.convert_contacts(orm_group.contacts.order_by(self.ORMContact.contact_id))

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.select_group_by_id(group.group_id)
        return self.convert_contacts(select(c for c in self.ORMContact
                                            if c.deprecated is None and orm_group not in c.groups))

    def select_contact_by_id(self, contact):
        return list(select(c for c in self.ORMContact if c.contact_id == contact.contact_id))[0]

    @db_session
    def get_groups_for_contact(self, contact):
        orm_contact = self.select_contact_by_id(contact)
        return self.convert_groups(orm_contact.groups.order_by(self.ORMGroup.group_id))

    @db_session
    def count_contacts_and_groups_links(self):
        return self.db.select("select count(*) from address_in_groups")

    @db_session
    def get_first_group_with_contacts(self):
        if self.count_contacts_and_groups_links():
            group_id = self.db.select("select group_id from address_in_groups")[0]
            return self.convert_groups([self.select_group_by_id(group_id)])[0]
        else:
            return None
